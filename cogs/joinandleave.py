import discord
from discord.ext import commands


class join_leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#join

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "join-leave":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="WELCOME",
                    value=
                    f"{member.mention} has joined ***{member.guild.name}*** ",
                    inline=False)
                embed.set_thumbnail(
                    url=
                    "https://gifimage.net/wp-content/uploads/2017/09/anime-hello-gif-9.gif"
                )
                embed.set_footer(text="Have fun in the server!")
                await channel.send(embed=embed)
            elif str(channel) == "welcome":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="WELCOME",
                    value=
                    f"{member.mention} has joined ***{member.guild.name}***",
                    inline=False)
                embed.set_thumbnail(
                    url=
                    "https://gifimage.net/wp-content/uploads/2017/09/anime-hello-gif-9.gif"
                )
                embed.set_footer(text="Have fun in the server!")
                await channel.send(embed=embed)
            elif str(channel) == "🎊│welcome":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="WELCOME",
                    value=
                    f"{member.mention} has joined ***{member.guild.name}***",
                    inline=False)
                embed.set_thumbnail(
                    url=
                    "https://gifimage.net/wp-content/uploads/2017/09/anime-hello-gif-9.gif"
                )
                embed.set_footer(text="Have fun in the server!")
                await channel.send(embed=embed)


#leave

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "join-leave":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="GOODBYE",
                    value=
                    f"{member.name} has left ***{member.guild.name}*** :cry:",
                    inline=False)
                embed.set_image(
                    url=
                    "https://media.giphy.com/media/26Ff5T4IoDXKMm20E/giphy.gif"
                )
                embed.set_footer(text="We gonna miss you")
                await channel.send(embed=embed)
            elif str(channel) == "welcome":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="GOODBYE",
                    value=
                    f"{member.name} has left ***{member.guild.name}*** :cry:",
                    inline=False)
                embed.set_image(
                    url=
                    "https://media.giphy.com/media/26Ff5T4IoDXKMm20E/giphy.gif"
                )
                embed.set_footer(text="We gonna miss you ")
                await channel.send(embed=embed)
            elif str(channel) == "👋│goodbye":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(
                    name="GOODBYE",
                    value=
                    f"{member.name} has left ***{member.guild.name}*** :cry:",
                    inline=False)
                embed.set_image(
                    url=
                    "https://media.giphy.com/media/26Ff5T4IoDXKMm20E/giphy.gif"
                )
                embed.set_footer(text="We gonna miss you ")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def  on_guild_join(self, guild):
        await guild.create_role(name="Government")
        await guild.create_role(name="jailed")




def setup(bot):
    bot.add_cog(join_leave(bot))
