import discord
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from discord.ext import commands
import os


class image_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def wanted(self, ctx, user: discord.Member = None):
      if user is None:
        user = ctx.author
      wanted = Image.open("images/wanted.png")

      asset = user.avatar_url_as(size = 128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)

      pfp = pfp.resize((490,490))

      wanted.paste(pfp, (120,270))

      wanted.save("wanted_profile.png")

      await ctx.send(file = discord.File("wanted_profile.png"))
      os.remove("wanted_profile.png")


    @commands.command(name = "abandon", aliases = ["aban"])
    @commands.guild_only()
    async def abandon(self, ctx, *, text = None ):
      if text == None:
        await ctx.send("please enter some text")
        
      img = Image.open("images/abandon.png")
      draw = ImageDraw.Draw(img)

      font_type = ImageFont.truetype("fonts/arial.ttf", 20)
      draw.text((20,420), text, (0, 0, 0), font=font_type)

      img.save("aban.png")
      await ctx.send(file = discord.File("aban.png"))
      os.remove("aban.png")



def setup(bot):
    bot.add_cog(image_fun(bot))
