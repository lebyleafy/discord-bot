import discord
from discord.ext import commands
import math
import asyncio



class Statics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def members(self ,ctx):
     members = [str(m) for m in ctx.guild.members]
     per_page = 10  # 10 members per page
     pages = math.ceil(len(members) / per_page)
     cur_page = 1
     chunk = members[:per_page]
     linebreak = "\n"
     message = await ctx.send(
        f"```Page {cur_page}/{pages}:\n{linebreak.join(chunk)}```")
     await message.add_reaction("◀️")
     await message.add_reaction("▶️")
     active = True

     def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # or you can use unicodes, respectively: "\u25c0" or "\u25b6"

     while active:
        try:
            reaction, user = await self.bot.wait_for("reaction_add",
                                                     timeout=60,
                                                     check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page != pages:
                    chunk = members[(cur_page - 1) * per_page:cur_page *
                                    per_page]
                else:
                    chunk = members[(cur_page - 1) * per_page:]
                await message.edit(
                    content=
                    f"```Page {cur_page}/{pages}:\n{linebreak.join(chunk)}```")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                chunk = members[(cur_page - 1) * per_page:cur_page * per_page]
                await message.edit(
                    content=
                    f"```Page {cur_page}/{pages}:\n{linebreak.join(chunk)}```")
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            active = False
    
    #server stat

    @commands.command()
    @commands.guild_only()
    async def serverstats(self, ctx):
        true_members = 0
        for member in ctx.guild.members:
            if not member.bot:
                true_members += 1
        bot_members = 0
        for member in ctx.guild.members:
            if member.bot:
                bot_members += 1
        embed = discord.Embed(title=f"Stats of: {ctx.guild.name}")
        embed.add_field(name="Users:",
                        value=ctx.guild.member_count,
                        inline=False)
        embed.add_field(name="Members:", value=true_members, inline=False)
        embed.add_field(name="Bots:", value=bot_members, inline=False)
        embed.add_field(name="Channels:",
                        value=len(ctx.guild.channels),
                        inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Statics(bot))
