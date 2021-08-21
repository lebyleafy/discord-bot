import discord
import os
import requests
import json
import random
import pyjokes
from online import keep_alive
import wolframalpha
from discord.ext import commands
import wikipedia
from PyDictionary import PyDictionary
import reply_bot
import praw
from translate import Translator


#create bot
intents = discord.Intents().all()
commands = commands.Bot(command_prefix=commands.when_mentioned_or("rba."), intents=intents)
commands.remove_command("help")
reddit = praw.Reddit(client_id='6KPuXtvipyTjhA',
                     client_secret='gDP_UibkLFxRlAJ2fcXgnehpIKXyzA',
                     user_agent='leafyBOT')


#help
@commands.command()
async def help(ctx):
    page1 = discord.Embed(
        title="Help",
        description=
        "***All the commands are here, if you have any question [click here](https://shrekis.life/WEHAIV)***",
        color=discord.Colour.orange())
    page1.set_thumbnail(url="https://acegif.com/wp-content/uploads/2020/b72nv6/partyparrt-24.gif")
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
    page1.add_field(
        name="Music :musical_note:",
        value="``plays music from youtube``")
    page1.add_field(name="Image :frame_photo:",
                    value="``reddit picture``")
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
        value="``rba.rps <rock, paper, scissors,> to play rock-paper-scissors``")
    page2.set_footer(text="2/8")

    #Annoying
    page3 = discord.Embed(
        title="Annoying :face_with_symbols_over_mouth:",
        description="***How to use Annoying command and how's it work***",
        color=discord.Colour.orange())
    page3.add_field(
        name="rba.spam <number><value>",
        value=
        "``Don't overuse this thing, it spams @everyone on your demand.``")
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
        value="``rba.wiki <keywords>, it gives you information form wikipedia.``")
    page4.add_field(
        name="rba.dict :book:",
        value="``rba.dict <keywords>, it gives you information about that word.``"
    )
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
    page6.add_field(name='rba.skip',
                    value='``skips the current song``')
    page6.add_field(name='rba.pause',
                    value="``pauses the song``")
    page6.add_field(name='rba.resume',
                    value="``resume the song``")
    page6.add_field(name='rba.queue or rba.playlist',
                    value="``shows the play list``")
    page6.add_field(name='rba.np',
                    value="``shows the current song``")
    page6.add_field(name='rba.leave',
                    value="``bot leaves the channel``")
    
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
    page8.add_field(name="rba.leafy",
                    value="``send leafy picture when he goes leafy mode``")
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


#rock paper scissors
@commands.command()
async def rps(ctx, arg):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if arg in possible_actions:
        await ctx.send(f"\nYou chose {arg}, leafy chose {computer_action}.\n")
        if arg == computer_action:
            await ctx.send(f"Both players selected {arg}. It's a tie!")
        elif arg == "rock":
            if computer_action == "scissors":
                await ctx.send("Rock smashes scissors! You just fucky man.")
            else:
                await ctx.send("Paper covers rock! hahaha noov.")
        elif arg == "paper":
            if computer_action == "rock":
                await ctx.send(
                    "Paper covers rock! WHAT? there is no next time doe")
            else:
                await ctx.send("Scissors cuts paper! My name is nt.")
        elif arg == "scissors":
            if computer_action == "paper":
                await ctx.send(
                    "Scissors cuts paper! What the fuck how could you win me?")
            else:
                await ctx.send(
                    "Rock smashes scissors! Haha u just can't beat me NOOB.")
    else:
        await ctx.send("dude thats wrong syntax, fucking dumbass")


#meme form reddit
@commands.command()
async def meme(ctx):
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
@commands.command()
async def redi(ctx, arg):
    memes_submissions = reddit.subreddit(str(arg)).hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        a = submission.url
        b = submission.title
    embed = discord.Embed(title=b, color=0xE38F8F)
    embed.set_image(url=a)
    await ctx.send(embed=embed)

#tell quote
@commands.command()
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" +"**"+ json_data[0]['a'] +"**" 
    await ctx.send(quote)


#tell joke
@commands.command()
async def joke(ctx):
    joke = (pyjokes.get_joke())
    await ctx.send(joke)


#roast
@commands.command()
async def roast(ctx, arg):
    await ctx.send(
        f"{arg} {random.choice(reply_bot.roast_ppl)}  -**{ctx.author.name}**")

@commands.command()
async def praise(ctx):
  await ctx.send(random.choice(reply_bot.praise))


#spam
@commands.command()
async def spam(ctx, arg1, *arg2):
    a = ' '.join(arg2)
    num = int(arg1)
    if num <= 5:
        for i in range(0, num):
            await ctx.send(str(a))
    elif num > 5:
        await ctx.send("haha no, you not gonna overload me XD")
        await ctx.send("leafy is not that dumb lol, btw maximum is 5 times")
    else: 
      await ctx.send("wrong syntax, stupid")


#wolframalpha wiki
@commands.command()
async def asks(ctx, *arg):
    a = ' '.join(arg)
    app_id = 'T8TJE5-6V67WHUAHT'
    client = wolframalpha.Client(app_id)
    res = client.query(a)
    answer = next(res.results).text
    await ctx.send(answer)


#wikipedia
@commands.command()
async def wiki(ctx, arg):
    a = ("```" + (wikipedia.summary((arg), sentences=5)) + "```")
    await ctx.send(a)


#dictionary
@commands.command()
async def dict(ctx, arg):
    dictionary = PyDictionary()
    await ctx.send(dictionary.meaning(arg))


@commands.command()
async def leafy_quote(ctx):
    await ctx.send(random.choice(reply_bot.leafyquote) + "** -leafy**")


@commands.command()
async def trans(ctx, lan1, lan2, *text):
    a = ' '.join(text)
    translator = Translator(from_lang=lan1, to_lang=lan2)
    translation = translator.translate(a)
    await ctx.send(translation)


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

    await commands.process_commands(message)


#bot ready
@commands.event
async def on_ready():
    print('We have logged in as {0.user}'.format(commands))
    await commands.change_presence(status=discord.Status.idle,activity=discord.Game(name="UR MOM | rba.help"))
    commands.load_extension("music")
   


keep_alive()
commands.run(os.getenv('TOKEN'))
