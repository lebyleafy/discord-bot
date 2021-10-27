import discord
from discord.ext import commands
from animec import *


class Anime_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#waifu pic
    @commands.command(name="randomwaifu", aliases=["rw"])
    @commands.guild_only()
    async def waifu_pics(self, ctx):
        a = Waifu().random()
        await ctx.send(a)

#untagged waifu
    @commands.command(name="untaggedwaifu", aliases=["uw"])
    @commands.guild_only()
    async def waifu_pics(self, ctx):
        a = Waifu().waifu()
        await ctx.send(a)

#slap
    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().slap()
            embed = discord.Embed(title=f"{ctx.author} slapped {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#kiss
    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().kiss()
            embed = discord.Embed(title=f"{ctx.author} kissed {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#hug
    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().hug()
            embed = discord.Embed(title=f"{ctx.author} hugged {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#high5
    @commands.command(name="highfive")
    @commands.guild_only()
    async def high5(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().highfive()
            embed = discord.Embed(title=f"{ctx.author} high-fived {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#kick
    @commands.command()
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().kick()
            embed = discord.Embed(title=f"{ctx.author} kicked {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#kill
    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().kill()
            embed = discord.Embed(title=f"{ctx.author} killed {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#pat
    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().pat()
            embed = discord.Embed(title=f"{ctx.author} patted {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#licked
    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().lick()
            embed = discord.Embed(title=f"{ctx.author} licked {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

#bully    
    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("you have to mention someone")
        else:
            a = str(user)
            b = Waifu().bully()
            embed = discord.Embed(title=f"{ctx.author} bullied {a}")
            embed.set_image(url=str(b))
            await ctx.send(embed=embed)

    #bully    
    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        b = Waifu().neko()
        await ctx.send(b)


#character search
    @commands.command(name="charsearch",
                      aliases=["cs", "chars", "char search"])
    @commands.guild_only()
    async def character_search(self, ctx, *arg):
        try:
            result = Charsearch(arg)
            embed = discord.Embed(title=result.title)
            embed.set_image(url=str(result.image_url))
            embed.add_field(name="Info:", value=result.url, inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send(
                "you have to send the full name of the character or your character doesn't exist"
            )


def setup(bot):
    bot.add_cog(Anime_fun(bot))
