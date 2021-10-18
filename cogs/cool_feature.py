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

reddit = praw.Reddit(client_id='6KPuXtvipyTjhA',
                     client_secret='gDP_UibkLFxRlAJ2fcXgnehpIKXyzA',
                     user_agent='leafyBOT')


class cool_Feature(commands.Cog):

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}
#rock paper scissors

    @commands.command()
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
    async def quote_(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + "**" + json_data[0]['a'] + "**"
        await ctx.send(quote)

#tell joke

    @commands.command()
    async def joke(self, ctx):
        joke = (pyjokes.get_joke())
        await ctx.send(joke)

#roast

    @commands.command(name='roast', aliases=['r'])
    async def roast(self, ctx, arg):
        await ctx.send(
            f"{arg} {random.choice(reply_bot.roast_ppl)}  -**{ctx.author.name}**"
        )

#praise

    @commands.command()
    async def praise(self, ctx):
        await ctx.send(random.choice(reply_bot.praise))

#spam

    @commands.command()
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
    async def asks(self, ctx, *arg):
        a = ' '.join(arg)
        app_id = 'T8TJE5-6V67WHUAHT'
        client = wolframalpha.Client(app_id)
        res = client.query(a)
        answer = next(res.results).text
        await ctx.send(answer)

#wikipedia

    @commands.command()
    async def wiki(self, ctx, arg):
        a = ("```" + (wikipedia.summary((arg), sentences=5)) + "```")
        await ctx.send(a)

#user avatar

    @commands.command(name='avatar', aliases=['ava'])
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        userAvatarUrl = avamember.avatar_url
        embed = discord.Embed(title=f"{avamember}'s avatar", color=0x2B59B)
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)

#dictionary

    @commands.command()
    async def dict(self, ctx, arg):
        dictionary = PyDictionary()
        await ctx.send(dictionary.meaning(arg))

#leafy quote

    @commands.command()
    async def leafy_quote(self, ctx):
        await ctx.send(random.choice(reply_bot.leafyquote) + "** -leafy**")


#translate

    @commands.command()
    async def trans(self, ctx, lan1, lan2, *text):
        a = ' '.join(text)
        translator = Translator(from_lang=lan1, to_lang=lan2)
        translation = translator.translate(a)
        await ctx.send(translation)


def setup(bot):
    bot.add_cog(cool_Feature(bot))