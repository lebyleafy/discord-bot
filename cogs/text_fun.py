import discord, asyncio, random, time, datetime, binascii
from discord.ext import commands
from discord.ext.commands import clean_content
import reply_bot

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''

    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(
                    MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


class TextConverters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mock'])
    @commands.guild_only()
    async def drunkify(self, ctx, *, s):
        lst = [str.upper, str.lower]
        newText = await commands.clean_content().convert(
            ctx, ''.join(random.choice(lst)(c) for c in s))
        if len(newText) <= 380:
            await ctx.send(newText)
        else:
            try:
                await ctx.author.send(newText)
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command()
    @commands.guild_only()
    async def expand(self, ctx, num: int, *, s: clean_content):
        spacing = ""
        if num > 0 and num <= 5:
            for _ in range(num):
                spacing += " "
            result = spacing.join(s)
            if len(result) <= 200:
                await ctx.send(result)
            else:
                try:
                    await ctx.author.send(result)
                    await ctx.send(
                        f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                    )
                except Exception:
                    await ctx.send(
                        f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                    )
        else:
            await ctx.send(
                "```fix\nError: The number can only be from 1 to 5```")

    @commands.command()
    @commands.guild_only()
    async def reverse(self, ctx, *, s: clean_content):
        result = await commands.clean_content().convert(ctx, s[::-1])
        if len(result) <= 350:
            await ctx.send(f"{result}")
        else:
            try:
                await ctx.author.send(f"{result}")
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command(name="texttohex", aliases=["tth"])
    @commands.guild_only()
    async def texttohex(self, ctx, *, s):
        try:
            hexoutput = await commands.clean_content().convert(
                ctx, (" ".join("{:02x}".format(ord(c)) for c in s)))
        except Exception as e:
            await ctx.send(
                f"**Error: `{e}`. This probably means the text is malformed. Sorry, you can always try here: http://www.unit-conversion.info/texttools/hexadecimal/#data**"
            )
        if len(hexoutput) <= 479:
            await ctx.send(f"```fix\n{hexoutput}```")
        else:
            try:
                await ctx.author.send(f"```fix\n{hexoutput}```")
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command(name="hextotext", aliases=["htt"])
    @commands.guild_only()
    async def hextotext(self, ctx, *, s):
        try:
            cleanS = await commands.clean_content().convert(
                ctx,
                bytearray.fromhex(s).decode())
        except Exception as e:
            await ctx.send(
                f"**Error: `{e}`. This probably means the text is malformed. Sorry, you can always try here: http://www.unit-conversion.info/texttools/hexadecimal/#data**"
            )
        if len(cleanS) <= 479:
            await ctx.send(f"```{cleanS}```")
        else:
            try:
                await ctx.author.send(f"```{cleanS}```")
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command(name="texttobinary", aliases=["ttb"])
    @commands.guild_only()
    async def texttobinary(self, ctx, *, s):
        try:
            cleanS = await commands.clean_content().convert(
                ctx, ' '.join(format(ord(x), 'b') for x in s))
        except Exception as e:
            await ctx.send(
                f"**Error: `{e}`. This probably means the text is malformed. Sorry, you can always try here: http://www.unit-conversion.info/texttools/convert-text-to-binary/#data**"
            )
        if len(cleanS) <= 479:
            await ctx.send(f"```fix\n{cleanS}```")
        else:
            try:
                await ctx.author.send(f"```fix\n{cleanS}```")
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command(name="binarytotext", aliases=["btt"])
    @commands.guild_only()
    async def binarytotext(self, ctx, *, s):
        try:
            cleanS = await commands.clean_content().convert(
                ctx, ''.join([chr(int(s, 2)) for s in s.split()]))
        except Exception as e:
            await ctx.send(
                f"**Error: `{e}`. This probably means the text is malformed. Sorry, you can always try here: http://www.unit-conversion.info/texttools/convert-text-to-binary/#data**"
            )
        if len(cleanS) <= 479:
            await ctx.send(f"```{cleanS}```")
        else:
            try:
                await ctx.author.send(f"```{cleanS}```")
                await ctx.send(
                    f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**"
                )
            except Exception:
                await ctx.send(
                    f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**"
                )

    @commands.command()
    @commands.guild_only()
    async def encrypt(self, ctx, *, arg):
        result = encrypt(arg.upper())
        await ctx.send(result)

    #decrypt
    @commands.command()
    @commands.guild_only()
    async def decrypt(self, ctx, *, arg):
        result = decrypt(arg)
        await ctx.send(result)

#purge

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention),
                       delete_after=20)
        await ctx.message.delete()


    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No permission")


def setup(bot):
    bot.add_cog(TextConverters(bot))
