import discord
from discord.ext import commands
class join_leave(commands.Cog):

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}
    @commands.Cog.listener()
    async def on_member_join(self, member):
     for channel in member.guild.channels:
        if str(channel) == "join-leave":
            embed = discord.Embed(color=0x4a3d9a)
            embed.add_field(name="WELCOME", value=f"***{member.name}*** has joined {member.guild.name}", inline=False)
            embed.set_thumbnail(
        url="https://gifimage.net/wp-content/uploads/2017/09/anime-hello-gif-9.gif")
            embed.set_footer(text="Have fun in the server!") 
            await channel.send(embed=embed)
        elif str(channel) == "welcome":
            embed = discord.Embed(color=0x4a3d9a)
            embed.add_field(name="WELCOME", value=f"***{member.name}*** has joined {member.guild.name}", inline=False)
            embed.set_thumbnail(
        url="https://gifimage.net/wp-content/uploads/2017/09/anime-hello-gif-9.gif")
            embed.set_footer(text="Have fun in the server!")
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(join_leave(bot))
