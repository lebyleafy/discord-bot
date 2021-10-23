import discord
import os
import random
from online import keep_alive
from discord.ext import commands
import reply_bot
import asyncio
import json
import math
from discord.ext.commands import cooldown, BucketType

with open("bank.json", "ab+") as ab:
    ab.close()
    f = open('bank.json', 'r+')
    f.readline()
    if os.stat("bank.json").st_size == 0:
        f.write("{}")
        f.close()
    else:
        pass


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="Wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("bank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]]
    return bal


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="withdraw", aliases=["wd", 'widr'])
    @commands.guild_only()
    async def withdrawmoney(self, ctx, amount=None):
        if amount is None:
            await ctx.send("Please enter the amount of money to withdraw")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You're not that rich lol")
            return
        if amount < 0:
            await ctx.send("Stop confusing me dude")
            return
        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1 * amount, "Bank")

        await ctx.send(f"You withdrew {amount}")

    @commands.command(name="deposit", aliases=["ds", "dep"])
    @commands.guild_only()
    async def depositmoney(self, ctx, amount=None):
        if amount is None:
            await ctx.send("Please enter the amount of money to deposit")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You're not that rich lol")
            return
        if amount < 0:
            await ctx.send("Stop confusing me dude")
            return
        await update_bank(ctx.author, -1 * amount)
        await update_bank(ctx.author, amount, "Bank")

        await ctx.send(f"deposited {amount}")

    @commands.command(name="balance", aliases=["bal", "money"])
    @commands.guild_only()
    async def balance(self, ctx):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["Wallet"]
        bank_amt = users[str(user.id)]["Bank"]

        em = discord.Embed(title=f"{ctx.author.name}'s balance.",
                           color=discord.Color.teal())
        em.add_field(name="Wallet Balance", value=wallet_amt)
        em.add_field(name="Bank Balance", value=bank_amt)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 18000, commands.BucketType.user)
    @commands.guild_only()
    async def beg(self, ctx):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        earnings = random.randrange(50)

        await ctx.send(f"Someone gave your {earnings} coins")

        users[str(user.id)]["Wallet"] += earnings

        with open("bank.json", 'w') as f:
            json.dump(users, f)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.guild_only()
    async def daily(self, ctx):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        earnings = random.randrange(150,300)

        await ctx.send(f"You earned {earnings} from daily")

        users[str(user.id)]["Wallet"] += earnings

        with open("bank.json", 'w') as f:
            json.dump(users, f)

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.guild_only()
    async def work(self, ctx):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        earnings = random.randrange(150)

        await ctx.send(f"You earned {earnings} after hardworking")

        users[str(user.id)]["Wallet"] += earnings

        with open("bank.json", 'w') as f:
            json.dump(users, f)

    @commands.command()
    @commands.cooldown(1, 43200, commands.BucketType.user)
    @commands.guild_only()
    async def rob(self, ctx, member: discord.Member):
        await open_account(ctx.author)
        await open_account(member)

        bal = await update_bank(member)

        if bal[0] < 100:
            await ctx.send("not worth it man")
            return
        else:
            earnings = random.randrange(0, bal[0])

            await update_bank(ctx.author, earnings)
            await update_bank(member, -1 * earnings)

            await ctx.send(f"You robbed {earnings}")
            return

    @commands.command()
    @commands.guild_only()
    async def give(self, ctx, member: discord.Member, amount=None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send("Please enter the amount")
            return

        bal = await update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("You're poor lol")
            return
        if amount < 0:
            await ctx.send("lol what? you mean rob?")

        await update_bank(ctx.author, -1 * amount)
        await update_bank(member, amount, "Bank")

        await ctx.send(f"You sent {amount}")

    @commands.command(pass_context=True, name="slot", aliases=["sl", "slots"])
    @commands.guild_only()
    async def slots(self, ctx, amount=None):

        if amount == None:
            await ctx.send("Please enter an amount")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        slots = ['bus', 'train', 'horse', 'tiger', 'monkey', 'cow']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]

        slotOutput = '| :{}: | :{}: | :{}: |\n'.format(slot1, slot2, slot3)

        ok = discord.Embed(title="Slots Machine", color=discord.Color(0xFFEC))
        ok.add_field(name="{}\nWon".format(slotOutput),
                     value=f'You won {2*amount} coins')

        won = discord.Embed(title="Slots Machine", color=discord.Color(0xFFEC))
        won.add_field(name="{}\nWon".format(slotOutput),
                      value=f'You won {3*amount} coins')

        lost = discord.Embed(title="Slots Machine",
                             color=discord.Color(0xFFEC))
        lost.add_field(name="{}\nLost".format(slotOutput),
                       value=f'You lost {1*amount} coins')

        if slot1 == slot2 == slot3:
            await update_bank(ctx.author, 3 * amount)
            await ctx.send(embed=won)
            return

        if slot1 == slot2:
            await update_bank(ctx.author, 2 * amount)
            await ctx.send(embed=ok)
            return

        else:
            await update_bank(ctx.author, -1 * amount)
            await ctx.send(embed=lost)
            return

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after/60, 2)} minutes'
            )

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after/3600, 2)} hours'
            )

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after/3600, 2)} hours'
            )

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after/3600, 2)} hours'
            )


def setup(bot):
    bot.add_cog(Economy(bot))
