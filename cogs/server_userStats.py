import discord
from discord.ext import commands
import math
import asyncio
from datetime import date


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

    @commands.command(invoke_without_command=True,
                      aliases=['user', 'uinfo', 'info', 'ui'])
    @commands.guild_only()
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author

        date_format = "%a, %d %b %Y %I:%M %p"
        age_format1 = "%y"
        age_format2 = "%m"
        today = date.today()

        d1 = int(today.strftime(age_format1))
        if today.strftime(age_format2) == user.created_at.strftime(
                age_format2) or today.strftime(
                    age_format2) > user.created_at.strftime(age_format2):
            b = (d1 - int(user.created_at.strftime(age_format1)))
        else:
            b = (d1 - int(user.created_at.strftime(age_format1))) - 1

        d2 = int(today.strftime(age_format2))
        if today.strftime(age_format2) > user.created_at.strftime(age_format2):
            b2 = d2 - (int(user.created_at.strftime(age_format2)))

        else:
            b2 = (int(user.created_at.strftime(age_format2)) - d2)

        embed = discord.Embed(color=0xdfa3ff, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Registered",
                        value=user.created_at.strftime(date_format))
        embed.add_field(name="Account age", value=f"{b} years, {b2} months")
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position",
                        value=str(members.index(user) + 1))
        embed.add_field(name="Joined",
                        value=user.joined_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
                            value=role_string,
                            inline=False)
        perm_string = ', '.join([
            str(p[0]).replace("_", " ").title() for p in user.guild_permissions
            if p[1]
        ])
        embed.add_field(name="Guild permissions",
                        value=perm_string,
                        inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Statics(bot))
