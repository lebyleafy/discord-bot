import discord
import requests
import json
import random
import pyjokes
import wolframalpha
from discord.ext import commands
import wikipedia
from PyDictionary import PyDictionary
import reply_bot
from translate import Translator
import qrcode
import qrcode.image.svg
import os
from aiohttp import ClientSession
from discord.ext.commands import cooldown, BucketType


client = wolframalpha.Client('T8TJE5-P2UV7G9TUE')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

num2emo = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


class cool_Feature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#tell quote

    @commands.command(name='quote')
    @commands.guild_only()
    async def quote_(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + "**" + json_data[0]['a'] + "**"
        await ctx.send(quote)

#tell joke

    @commands.command()
    @commands.guild_only()
    async def joke(self, ctx):
        joke = (pyjokes.get_joke())
        await ctx.send(joke)

#roast

    @commands.command(name='roast', aliases=['r'])
    @commands.guild_only()
    async def roast(self, ctx, arg):
        await ctx.send(
            f"{arg} {random.choice(reply_bot.roast_ppl)}  -**{ctx.author.name}**"
        )

#praise

    @commands.command()
    @commands.guild_only()
    async def praise(self, ctx):
        await ctx.send(random.choice(reply_bot.praise))

#spam

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def spam(self, ctx, arg1, *arg2):
        a = ' '.join(arg2)
        num = int(arg1)
        if num <= 5:
            for i in range(0, num):
                await ctx.send(str(a))
        elif num > 5:
            await ctx.send("haha no, you not gonna overload me XD")
            await ctx.send("leafy is not that dumb lol, btw maximum is 5 times"
                           )
        else:
            await ctx.send("wrong syntax, stupid")

#wolframalpha wiki

    @commands.command()
    @commands.guild_only()
    async def asks(self, ctx, *,arg):
      try:
        res = client.query(arg)
        answer = (next(res.results).text)
        await ctx.send(answer)
      except:
            await ctx.send("an error has occurred")
#wikipedia

    @commands.command()
    @commands.guild_only()
    async def wiki(self, ctx, *,arg):
        try:
            a = (wikipedia.summary(arg, sentences=1000))
            embed = discord.Embed(title=arg, description=a[0:5980])
            await ctx.send(embed=embed)
        except:
            await ctx.send("please more specific")

#user avatar

    @commands.command(name='avatar', aliases=['ava'])
    @commands.guild_only()
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        if avamember == None:
            avamember = ctx.author
        userAvatarUrl = avamember.avatar_url
        embed = discord.Embed(title=f"{avamember}'s avatar", color=0x2B59B)
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)

#dictionary

    @commands.command()
    @commands.guild_only()
    async def dict(self, ctx, arg):
        dictionary = PyDictionary()
        await ctx.send(dictionary.meaning(arg))

#leafy quote

    @commands.command(name="leafyquote", aliases=["lq", "leafy_quote"])
    @commands.guild_only()
    async def leafy_quote(self, ctx):
        await ctx.send(random.choice(reply_bot.leafyquote) + "** -leafy**")

#translate

    @commands.command()
    @commands.guild_only()
    async def trans(self, ctx, lan1, lan2, *text):
        a = ' '.join(text)
        translator = Translator(from_lang=lan1, to_lang=lan2)
        translation = translator.translate(a)
        await ctx.send(translation)

#level

    @commands.command()
    @commands.guild_only()
    async def rank(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'You have {lvl} social credits!')
        else:
            id = member.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member} has {lvl} social credits!')


#QR generator(@Dart (1202))

    @commands.command(name='createQR', aliases=['QR', 'qr'])
    @commands.guild_only()
    async def create_QR(self, ctx, *, arg):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=4,
        )
        try:
            qr.add_data(arg)
            qr.make(fit=True)
        except:
            ctx.send("something went wrong!")
        img = qr.make_image()
        img.save("code.png")
        file = discord.File('code.png')
        try:
            await ctx.send(file=file)
            os.remove("code.png")
        except:
            print("error creating your QR")

#urban dictionary

    @commands.command(name="Urban dictionary",
                      aliases=["urban", "urband", "ub"])
    @commands.guild_only()
    async def urbandictionary(self, ctx, *, term):
        url = 'https://mashape-community-urban-dictionary.p.rapidapi.com/define'
        querystring = {"term": term}
        headers = {
            'x-rapidapi-host':
            'mashape-community-urban-dictionary.p.rapidapi.com',
            'x-rapidapi-key':
            '053d5b3a94mshfec0a2023e4d0c3p199574jsn663cf953f492'
        }
        async with ClientSession() as session:
            async with session.get(url, headers=headers,
                                   params=querystring) as response:
                try:
                    r = await response.json()
                    definition1 = r['list'][0]['definition']
                    definition2 = r['list'][1]['definition']
                    definition3 = r['list'][2]['definition']
                    definition4 = r['list'][3]['definition']
                    definition5 = r['list'][4]['definition']

                    example1 = r['list'][0]['example']
                    example2 = r['list'][1]['example']
                    example3 = r['list'][2]['example']
                    example4 = r['list'][3]['example']
                    example5 = r['list'][4]['example']

                    embed = discord.Embed(title=f"Result for:   ***{term}***",
                                          color=0x206694)
                    embed.add_field(name=term,
                                    value=definition1[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example1[0:1024],
                                    inline=False)
                    embed.add_field(name=term,
                                    value=definition2[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example2[0:1024],
                                    inline=False)
                    embed.add_field(name=term,
                                    value=definition3[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example3[0:1024],
                                    inline=True)
                    embed.add_field(name=term,
                                    value=definition3[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example3[0:1024],
                                    inline=True)
                    embed.add_field(name=term,
                                    value=definition4[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example4[0:1024],
                                    inline=True)
                    embed.add_field(name=term,
                                    value=definition5[0:1024],
                                    inline=False)
                    embed.add_field(name="example: ",
                                    value=example5[0:1024],
                                    inline=True)

                    await ctx.send(embed=embed)

                except:
                    await ctx.send("no definiton for that")

#8ball

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        response = random.choice(reply_bot.ball_8)
        embed = discord.Embed(title=":8ball: The Magic 8 Ball has Spoken!")
        embed.add_field(name='Question: ', value=f'{question}', inline=True)
        embed.add_field(name='Answer: ', value=f'{response}', inline=False)
        await ctx.send(embed=embed)

#gay meter

    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        if user.id == 528225222525059102:
            await ctx.send(
                "huh you think leby didnt expected this? I'm a chad and straighter than your mom's dacing pole"
            )

        if user == ctx.author and user.id != 528225222525059102:
            embed = discord.Embed(
                title="Gay meter: ",
                description=
                f"You are {random.randrange(100)}% gay :gay_pride_flag:")
            await ctx.send(embed=embed)
        elif user.id != 528225222525059102:
            embed = discord.Embed(
                title="Gay meter: ",
                description=
                f"He is {random.randrange(100)}% gay :gay_pride_flag:")
            await ctx.send(embed=embed)

#penis size

    @commands.command()
    @commands.guild_only()
    async def penis(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        i = "8{}D".format("=" * random.randint(0, 30))
        embed = discord.Embed(title="Penis size: ", description=i)
        if user.id == 528225222525059102:
            embed = discord.Embed(title="Penis size: ",
                                  description="8{}D".format("=" * 48))
        await ctx.send(embed=embed)

#emojify text

    @commands.command()
    @commands.guild_only()
    async def emojify(self, ctx, *, text=None):
        if text is None:
            await ctx.send("please enter something")
        emojis = []
        for s in text:
            if s.isdecimal():
                emojis.append(f":{num2emo.get(s)}:")
            elif s.isalpha():
                emojis.append(f":regional_indicator_{s}:")
            else:
                emojis.append(s)
        await ctx.send(''.join(emojis))


#error

    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds'
            )


def setup(bot):
    bot.add_cog(cool_Feature(bot))
