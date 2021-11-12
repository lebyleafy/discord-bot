import discord
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO
from discord.ext import commands
import os
import sys

chars = ["B","S","#","&","@","$","%","*","!",":","."]

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

#achivement
    @commands.command(name = "achievement", aliases = ["achieve"])
    @commands.guild_only()
    async def achivement(self, ctx, *, text = None ):
      if text == None:
        await ctx.send("please enter some text")
        
      img = Image.open("images/cool.png")
      img = img.resize((640,128))
      draw = ImageDraw.Draw(img)

      font_type = ImageFont.truetype("fonts/minecraft.ttf", 27)
      draw.text((117,60), text, (255, 255, 255), font=font_type)

      img.save("achieve.png")
      await ctx.send(file = discord.File("achieve.png"))

      os.remove("achieve.png")
  #pixelate image
    @commands.command()
    @commands.guild_only()
    async def pixel(self, ctx, user: discord.Member = None):
      if user is None:
        user = ctx.author

      asset = user.avatar_url_as(size = 512)
      data = BytesIO(await asset.read())
      img = Image.open(data)

      imgSmall = img.resize((50,50),resample=Image.BILINEAR)

      result = imgSmall.resize(img.size,Image.NEAREST)

      result.save('pixel.png')
      await ctx.send(file = discord.File("pixel.png"))
      os.remove("pixel.png")


    @commands.command()
    @commands.guild_only()
    async def shit(self, ctx,* ,text = None):
      if text == None:
        await ctx.send("please enter some text")
        
      img = Image.open("images/shitstep.png")
      font_type = ImageFont.truetype("fonts/arial.ttf", 20) 

      txt=Image.new('L', (680,1062))
      d = ImageDraw.Draw(txt)
      d.text((1,50), text,  font=font_type, fill=255)
      w=txt.rotate(50,  expand=1)

      img.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)
      img.save("shit.png")
      await ctx.send(file = discord.File("shit.png"))

      os.remove("shit.png")

    @commands.command()
    @commands.guild_only()
    async def ascii(self, ctx, user: discord.Member = None):
      if user is None:
        user = ctx.author

      asset = user.avatar_url_as(size = 512)
      data = BytesIO(await asset.read())
      img = Image.open(data)

      width, height = img.size
      aspect_ratio = height/width
      new_width = 120
      new_height = aspect_ratio * new_width * 0.55
      img = img.resize((new_width, int(new_height)))
      img = img.convert('L')

      pixels = img.getdata()

      new_pixels = [chars[pixel//25] for pixel in pixels]
      new_pixels = ''.join(new_pixels)

      new_pixels_count = len(new_pixels)
      ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
      ascii_image = "\n".join(ascii_image)

      with open("ascii_image.txt", "w") as f:
       f.write(ascii_image)
      await ctx.send(file = discord.File("ascii_image.txt"))
      os.remove("ascii_image.txt")



def setup(bot):
    bot.add_cog(image_fun(bot))
