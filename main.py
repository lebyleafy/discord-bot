import discord
import os
import random
from online import keep_alive
from discord.ext import commands
import reply_bot
import asyncio
import json
import math
import time
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands.context import Context
from discord.ext.commands import has_permissions
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from os import listdir
from discord import Guild
import json
from discord_components import DiscordComponents, Button, ButtonStyle
#create bot
intents = discord.Intents().all()
intents.members = True
commands = commands.Bot(command_prefix=commands.when_mentioned_or("rba."),
                        intents=intents,
                        help_command=None)


initial_extensions = [
    'cogs.music', 'cogs.cool_feature', 'cogs.joinandleave', 'cogs.subreddit',
    'cogs.fun_anime', 'cogs.economy_system', 'cogs.help',
    'cogs.server_userStats', 'cogs.minigames', 'cogs.sussygame',
    'cogs.image_fun', 'cogs.text_fun', 'cogs.maths'
]

with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json', 'r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
        f.write("{}")
        f.close()
    else:
        pass

with open('users.json', 'r') as f:
    users = json.load(f)


async def add_experience(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
    users[f'{user.id}']['experience'] += 4


async def level_up(users, user, message):
    experience = users[f'{user.id}']["experience"]
    lvl_start = users[f'{user.id}']["level"]
    lvl_end = int(experience**(1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(
            f':tada: {user.mention} has earned total of {lvl_end} social credits. Congrats! :tada:'
        )
        users[f'{user.id}']["level"] = lvl_end


@commands.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("that command doesn't exist lol")


@commands.event
async def on_message(message):
    if message.author == commands.user:
        return
    if message.author.bot:
        return
    if isinstance(
            message.channel,
            discord.channel.DMChannel) and message.author != commands.user:
        await message.channel.send(
            "this is a DM, you can't use my feature here")
    msg = message.content
    if msg in reply_bot.greetings:
            await message.channel.send(random.choice(reply_bot.greetings_back))
    if msg in reply_bot.say_bye:
            await message.channel.send(random.choice(reply_bot.bye))
    if msg in reply_bot.how_are_you:
            await message.channel.send(
                random.choice(reply_bot.how_are_you_reply))
    if msg in reply_bot.bad_chat:
            await message.channel.send(random.choice(reply_bot.bad_reply))
    if msg in reply_bot.fuck:
            await message.channel.send(random.choice(reply_bot.fuck_reply))
    if msg in reply_bot.wtf:
            await message.channel.send(random.choice(reply_bot.wtf_reply))
    if msg in reply_bot.who_are_you:
            await message.channel.send(
                random.choice(reply_bot.who_are_you_reply))
    if msg in reply_bot.who_is_leafy:
            await message.channel.send(
                random.choice(reply_bot.who_is_leafy_reply))
    if msg in reply_bot.stfu:
            await message.channel.send(random.choice(reply_bot.stfu_reply))
    if msg in reply_bot.who_asked:
            await message.channel.send(random.choice(reply_bot.who_asked_reply)
                                       )
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
    await commands.process_commands(message)


#load feature
if __name__ == '__main__':
    for extension in initial_extensions:
        commands.load_extension(extension)


#bot ready
@commands.event
async def on_ready():
    print('We have logged in as {0.user}'.format(commands))
    await commands.change_presence(
        status=discord.Status.idle,
        activity=discord.Streaming(
            name=f"in {len(commands.guilds)} servers| rba.help",
            url='https://www.youtube.com/watch?v=9jrO58mg-Qg'))
    DiscordComponents(commands)

keep_alive()
commands.run(os.getenv('TOKEN'))
