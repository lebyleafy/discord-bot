import discord
import os
import random
from online import keep_alive
from discord.ext import commands
import reply_bot
import asyncio
import json
#create bot
intents = discord.Intents().all()
commands = commands.Bot(command_prefix=commands.when_mentioned_or("rba."),
                        intents=intents)
commands.remove_command("help")

#help
@commands.command()
async def help(ctx):
    page1 = discord.Embed(
        title="Help",
        description=
        "***All the commands are here, if you have any question [click here](https://shrekis.life/WEHAIV)***",
        color=discord.Colour.orange())
    page1.set_thumbnail(
        url=
        "https://acegif.com/wp-content/uploads/2020/b72nv6/partyparrt-24.gif")
    page1.add_field(
        name="Fun :smile:",
        value="``joke, memes, quote, leafy's quote, 'rock,paper,scissors'``")
    page1.add_field(name="Annoying :face_with_symbols_over_mouth:",
                    value="``spam, roast``")
    page1.add_field(name="Wiki :thinking:", value="``asks, wiki, urb, dict``")
    page1.add_field(name="Chat :speech_balloon:",
                    value='``say "hi", "bye", "how are you?"``')
    page1.add_field(name="Reply :busts_in_silhouette: ",
                    value="``stupid leafy hasn't add it yet.``")
    page1.add_field(name="Music :musical_note:",
                    value="``plays music from youtube``")
    page1.add_field(name="Image :frame_photo:", value="``reddit picture``")
    page1.set_footer(text="1/8")

    #Fun
    page2 = discord.Embed(
        title="Fun :smile:",
        description="***How to use Fun command and how's it work***",
        color=discord.Colour.green())
    page2.add_field(name="rba.joke :clown:",
                    value="``use this to make bot tell some nerdy joke``")
    page2.add_field(name="rba.quote :bulb:",
                    value="``make bot tell some quote to inspire youself.``")
    page2.add_field(name="rba.meme :ok_hand:", value="`send random memes.`")
    page2.add_field(
        name="rba.leafy_quote :leaves:",
        value=
        "``bot tells quote from the smartest person in this server with extreme CS:GO skill, btw he's the best programmer tho.``"
    )
    page2.add_field(
        name="rba.rps :fist: :v: :raised_hand: ",
        value="``rba.rps <rock, paper, scissors,> to play rock-paper-scissors``"
    )
    page2.set_footer(text="2/8")

    #Annoying
    page3 = discord.Embed(
        title="Annoying :face_with_symbols_over_mouth:",
        description="***How to use Annoying command and how's it work***",
        color=discord.Colour.orange())
    page3.add_field(
        name="rba.spam <number><value>",
        value="``Don't overuse this thing, it spams @everyone on your demand.``"
    )
    page3.add_field(name="rba.roast <@'name'>",
                    value="``use this to roast your friend``")
    page3.set_footer(text="3/8")

    #Wiki
    page4 = discord.Embed(
        title="Wiki :thinking:",
        description="***How to use Wiki command and how's it work***",
        color=discord.Colour.green())
    page4.add_field(
        name="rba.asks :question:",
        value=
        "``rba.asks <question>, it can answer *mostly* anything but sometimes it can't answer your question.``"
    )
    page4.add_field(
        name="rba.wiki :grey_question:",
        value=
        "``rba.wiki <keywords>, it gives you information form wikipedia.``")
    page4.add_field(
        name="rba.dict :book:",
        value=
        "``rba.dict <keywords>, it gives you information about that word.``")
    page4.add_field(
        name="rba.urb :city_dusk:",
        value=
        "``rba.urb <keywords>, it gives you information about that word from urban dictionary.``"
    )
    page4.set_footer(text="4/8")

    #Chat
    page5 = discord.Embed(
        title="Chat :speech_balloon:",
        description="***How to use Chat command and how's it work***",
        color=discord.Colour.orange())
    page5.add_field(name='say "hi","hello",etc.',
                    value="``it greets you back.``")
    page5.add_field(name='say "bye", "goodbye",etc.',
                    value='``it says goodbye back or "something" else.``')
    page5.add_field(name='say "how are you BOT?"',
                    value="``it tell you how's it feels.``")
    page5.set_footer(text="5/8")

    #Music
    page6 = discord.Embed(
        title="Music :musical_note:",
        description="***How to use Music command and how's it work***",
        color=discord.Colour.green())
    page6.add_field(name='rba.join',
                    value="``bot join the voicechat channel you are in``")
    page6.add_field(name='rba.play <name> or <link>',
                    value="``to play music from youtube``")
    page6.add_field(name='rba.skip', value='``skips the current song``')
    page6.add_field(name='rba.pause', value="``pauses the song``")
    page6.add_field(name='rba.resume', value="``resume the song``")
    page6.add_field(name='rba.queue or rba.playlist',
                    value="``shows the play list``")
    page6.add_field(name='rba.np', value="``shows the current song``")
    page6.add_field(name='rba.leave', value="``bot leaves the channel``")

    page6.set_footer(text="6/8")

    #Reply
    page7 = discord.Embed(
        title="Reply :busts_in_silhouette:",
        description="***How to use Reply command and how's it work***",
        color=discord.Colour.orange())
    page7.add_field(
        name="rba.r",
        value=
        "``lazyass leafy hasn't added it yet, but if you wonder what is it. Basically, it's reply you with the seted word``"
    )
    page7.set_footer(text="7/8")

    #Image
    page8 = discord.Embed(
        title="Image :frame_photo:",
        description="***How to use Image command and how's it work***",
        color=discord.Colour.green())
    page8.add_field(name="rba.redi <value>",
                    value="``it send picture from reddit.``")
    
    page8.set_footer(text="8/8")

    pages = [page1, page2, page3, page4, page5, page6, page7, page8]

    message = await ctx.send(embed=page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 7:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 7
            await message.edit(embed=pages[i])

        try:
            reaction, user = await commands.wait_for('reaction_add',
                                                     timeout=60.0,
                                                     check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()

with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 

async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 3

 
async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.channel.send(f':tada: {user.mention} has reached level {lvl_end}. Congrats! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@commands.command(name='rank', aliases=['lvl','levels','level'])
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} You are at level {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')


@commands.event
async def on_message(message):
    
    msg = message.content
    if message.author == commands.user:
        return
    if message.author.bot: return
    if msg in reply_bot.greetings:
        await message.channel.send(random.choice(reply_bot.greetings_back))
    if msg in reply_bot.say_bye:
        await message.channel.send(random.choice(reply_bot.bye))
    if msg in reply_bot.how_are_you:
        await message.channel.send(random.choice(reply_bot.how_are_you_reply))
    if msg in reply_bot.bad_chat:
        await message.channel.send(random.choice(reply_bot.bad_reply))
    if msg in reply_bot.fuck:
        await message.channel.send(random.choice(reply_bot.fuck_reply))
    if msg in reply_bot.wtf:
        await message.channel.send(random.choice(reply_bot.wtf_reply))
    if msg in reply_bot.who_are_you:
        await message.channel.send(random.choice(reply_bot.who_are_you_reply))
    if msg in reply_bot.who_is_leafy:
        await message.channel.send(random.choice(reply_bot.who_is_leafy_reply))
    if msg in reply_bot.stfu:
        await message.channel.send(random.choice(reply_bot.stfu_reply))
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)


    await commands.process_commands(message)


#bot ready
@commands.event
async def on_ready():
    print('We have logged in as {0.user}'.format(commands))
    await commands.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(name="UR MOM | rba.help"))
    commands.load_extension("music")
    commands.load_extension("joinandleave")
    commands.load_extension("cool_feature")



keep_alive()
commands.run(os.getenv('TOKEN'))
