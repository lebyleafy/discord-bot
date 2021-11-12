import discord, datetime, time, aiohttp, asyncio, random
from discord.ext import commands
from random import randint
from random import choice
from urllib.parse import quote_plus
from collections import deque
import praw

reddit = praw.Reddit(client_id='6KPuXtvipyTjhA',
                     client_secret='gDP_UibkLFxRlAJ2fcXgnehpIKXyzA',
                     user_agent='leafyBOT')

acceptableImageFormats = [".png",".jpg",".jpeg",".gif",".gifv",".webm",".mp4","imgur.com"]
memeHistory = deque()
memeSubreddits = ["BikiniBottomTwitter", "memes", "2meirl4meirl", "deepfriedmemes", "MemeEconomy"]

async def getSub(self, ctx, sub):
        """Get stuff from requested sub"""
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://www.reddit.com/r{sub}/hot.json?limit=100") as response:
                    request = await response.json()

            attempts = 1
            while attempts < 5:
                if 'error' in request:
                    print("failed request {}".format(attempts))
                    await asyncio.sleep(2)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"https://www.reddit.com/r/{sub}/hot.json?limit=100") as response:
                            request = await response.json()
                    attempts += 1
                else:
                    index = 0

                    for index, val in enumerate(request['data']['children']):
                        if 'url' in val['data']:
                            url = val['data']['url']
                            urlLower = url.lower()
                            accepted = False
                            for j, v, in enumerate(acceptableImageFormats): #check if it's an acceptable image
                                if v in urlLower:
                                    accepted = True
                            if accepted:
                                if url not in memeHistory:
                                    memeHistory.append(url)  #add the url to the history, so it won't be posted again
                                    if len(memeHistory) > 63: #limit size
                                        memeHistory.popleft() #remove the oldest

                                    break #done with this loop, can send image
                    await ctx.send(memeHistory[len(memeHistory) - 1]) #send the last image
                    return
            await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

class SubredditFetcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.guild_only()
    async def showerthought(self, ctx):
      async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/showerthoughts/hot.json?limit=100") as response:
                request = await response.json()

        attempts = 1
        while attempts < 5:
            if 'error' in request:
                print("failed request {}".format(attempts))
                await asyncio.sleep(2)
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.reddit.com/r/showerthoughts/hot.json?limit=100") as response:
                        request = await response.json()
                attempts += 1
            else:
                index = 0

                for index, val in enumerate(request['data']['children']):
                    if 'title' in val['data']:
                        url = val['data']['title']
                        urlLower = url.lower()
                        accepted = False
                        if url == "What Is A Showerthought?":
                            accepted = False
                        elif url == "Showerthoughts is looking for new moderators!":
                            accepted = False
                        else:
                            accepted = True
                        if accepted:
                            if url not in memeHistory:
                                memeHistory.append(url)
                                if len(memeHistory) > 63:
                                    memeHistory.popleft()

                                break
                await ctx.send(memeHistory[len(memeHistory) - 1])
                return
        await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

    
    @commands.command(aliases=['dankmeme', 'dank'])
    @commands.guild_only()
    async def dankmemes(self, ctx):
        await getSub(self, ctx, 'dankmemes')
        
    @commands.command()
    @commands.guild_only()
    async def me_irl(self, ctx):
        await getSub(self, ctx, 'me_irl')

    @commands.command()
    @commands.guild_only()
    async def programmerhumor(self, ctx):
        await getSub(self, ctx, 'ProgrammerHumor')

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

def setup(bot):
    bot.add_cog(SubredditFetcher(bot))