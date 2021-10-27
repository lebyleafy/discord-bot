import discord
from discord.ext import commands
import random

def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def findimposter(self, ctx):
        """
        Impostors can sabotage the reactor, 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win.
        """

        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down!" , color=0xff0000)
        
        embed1.add_field(name = 'Red' , value= '<:Red:902851594599677992>' , inline=False)
        embed1.add_field(name = 'Blue' , value= '<:Blue:902851581739933696>' , inline=False)
        embed1.add_field(name = 'Lime' , value= '<:Lime:902851569542905886>' , inline=False)
        embed1.add_field(name = 'White' , value= '<:White:902851550135849000>' , inline=False)
        
        msg = await ctx.send(embed=embed1)
        
        # imposter : emoji
        emojis = {
            'red': '<:Red:902851594599677992>',
            'blue': '<:Blue:902851581739933696>',
            'lime': '<:Lime:902851569542905886>',
            'white': '<:White:902851550135849000>'
        }
        
        # pick the imposter
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
        
        # add all possible reactions
        for emoji in emojis.values():
            await msg.add_reaction(emoji)
        
        # check whether the correct user responded.
        # also check its a valid reaction.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try: 
           reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
           await msg.remove_reaction(reaction, user)
        
        except:
            # defeat, reactor meltdown
            description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
            embed = get_embed("Defeat", description, discord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory, correct answer
            if str(self.reacted) == emojis[imposter]:
                description = "**{0}** was the imposter...".format(imposter)
                embed = get_embed("Victory", description, discord.Color.blue())
                await ctx.send(embed=embed)

            # defeat, wrong answer
            else:
                for key, value in emojis.items(): 
                    if value == str(self.reacted):
                        description = "**{0}** was not the imposter...".format(key)
                        embed = get_embed("Defeat", description, discord.Color.red())
                        await ctx.send(embed=embed)
                        break


        await msg.clear_reactions()
def setup(bot):
    bot.add_cog(games(bot))