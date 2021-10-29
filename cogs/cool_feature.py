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
import praw
from translate import Translator
import qrcode
import qrcode.image.svg
import os
from aiohttp import ClientSession
from discord.ext.commands import cooldown, BucketType
import reply_bot

reddit = praw.Reddit(client_id='6KPuXtvipyTjhA',
                     client_secret='gDP_UibkLFxRlAJ2fcXgnehpIKXyzA',
                     user_agent='leafyBOT')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''

    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(
                    MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


class cool_Feature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#rock paper scissors

    @commands.command()
    @commands.guild_only()
    async def rps(self, ctx, arg):
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        if arg in possible_actions:
            await ctx.send(
                f"\nYou chose {arg}, leafy chose {computer_action}.\n")
            if arg == computer_action:
                await ctx.send(f"Both players selected {arg}. It's a tie!")
            elif arg == "rock":
                if computer_action == "scissors":
                    await ctx.send("Rock smashes scissors! You just fucky man."
                                   )
                else:
                    await ctx.send("Paper covers rock! hahaha noov.")
            elif arg == "paper":
                if computer_action == "rock":
                    await ctx.send(
                        "Paper covers rock! WHAT? there is no next time doe")
                else:
                    await ctx.send("Scissors cuts paper! My name is nt.")
            elif arg == "scissors":
                if computer_action == "paper":
                    await ctx.send(
                        "Scissors cuts paper! What the fuck how could you win me?"
                    )
                else:
                    await ctx.send(
                        "Rock smashes scissors! Haha u just can't beat me NOOB."
                    )
            else:
                await ctx.send("dude thats wrong syntax, fucking dumbass")

#meme form reddit

    @commands.command()
    @commands.guild_only()
    async def meme(self, ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
            a = submission.url
            b = submission.title
        embed = discord.Embed(title=b, color=0x2B59B)
        embed.set_image(url=a)
        await ctx.send(embed=embed)

#reddit image

    @commands.command(name='reddit', aliases=['redi'])
    @commands.guild_only()
    async def reddit(self, ctx, *arg):
        redimoment = ' '.join(arg)
        redi_submissions = reddit.subreddit(str(redimoment)).hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in redi_submissions if not x.stickied)
            a = submission.url
            b = submission.title
        embed = discord.Embed(title=b, color=0xE38F8F)
        embed.set_image(url=a)
        await ctx.send(embed=embed)

#tell quote

    @commands.command(name='quote', aliases=['qo'])
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
    @commands.cooldown(1, 5, commands.BucketType.user)
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
    async def asks(self, ctx, *arg):
        a = ' '.join(arg)
        app_id = 'T8TJE5-6V67WHUAHT'
        client = wolframalpha.Client(app_id)
        res = client.query(a)
        answer = next(res.results).text
        await ctx.send(answer)

#wikipedia

    @commands.command()
    @commands.guild_only()
    async def wiki(self, ctx, arg):
        try:
            a = (wikipedia.summary(arg, sentences=1000))
            embed = discord.Embed(title=arg, description=a[0:5900])
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

    @commands.command()
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

#morse decoder

#encrypt

    @commands.command()
    @commands.guild_only()
    async def encrypt(self, ctx, *, arg):
        result = encrypt(arg.upper())
        await ctx.send(result)

    #decrypt
    @commands.command()
    @commands.guild_only()
    async def decrypt(self, ctx, *, arg):
        result = decrypt(arg)
        await ctx.send(result)

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

    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        if user.id == 528225222525059102:
            await ctx.send(
                "huh you think leby didnt expected this? I'm a chad and straighter than your mom's dacing pole"
            )

        if user == ctx.author and user.id != 528225222525059102 :
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

    @commands.command()
    @commands.guild_only()
    async def penis(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        i = "8{}D".format("=" * random.randint(0, 30))
        embed = discord.Embed(title="Penis size: ",description=i)
        if user.id == 528225222525059102:
          embed = discord.Embed(title="Penis size: ",description="8{}D".format("=" * 48))
        await ctx.send(embed=embed)

    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds'
            )


def setup(bot):
    bot.add_cog(cool_Feature(bot))
