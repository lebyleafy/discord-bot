import discord
from discord.ext import commands
from datetime import date
'''Module for the info command.'''


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    bot.add_cog(Userinfo(bot))
