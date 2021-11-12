import matplotlib.pyplot as plt
import numpy as np
import discord
from discord.ext import commands
import os
from discord_components import Button, ButtonStyle
from math import *
import asyncio

def calculate(exp:str):
    result=''
    o=exp
    o=o.replace('π', str(pi))
    o=o.replace('τ', str(tau))
    o=o.replace('e', str(e))
    o=o.replace('×', '*')
    o=o.replace('÷', '/')
    o=o.replace('^2', '**2')
    o=o.replace('^3', '**3')
    o=o.replace('^', '**')
    o=o.replace('√', 'sqrt')
    try:
        result = eval(o, {'sqrt': sqrt})
    except:
        result=f"Syntax Error!\nDon't forget the sign(s) ('×', '÷', ...).\nnot: 3(9+1) but 3×(9+1)"
    return result

def input_formatter(original:str, new:str):
    if 'Syntax Error!' in original:
        original='|'
    lst=list(original)
    try:
        index=lst.index('|')
        lst.remove('|')
    except:
        index=0
    if new == '1':
        lst.insert(index, '1')
    elif new == '2':
        lst.insert(index, '2')
    elif new == '3':
        lst.insert(index, '3')
    elif new == '4':
        lst.insert(index, '4')
    elif new == '5':
        lst.insert(index, '5')
    elif new == '6':
        lst.insert(index, '6')
    elif new == '7':
        lst.insert(index, '7')
    elif new == '8':
        lst.insert(index, '8')
    elif new == '9':
        lst.insert(index, '9')
    elif new == '10':
        lst.insert(index, '10')
    elif new == '0':
        lst.insert(index, '0')
    elif new == '00':
        lst.insert(index, '00')
    elif new == '+':
        lst.insert(index, '+')
    elif new == '÷':
        lst.insert(index, '÷')
    elif new == '-':
        lst.insert(index, '-')
    elif new == '×':
        i=index-1
        try:
            if lst[i]=='×':
                lst.insert(index+1, '|')
                original=''.join(lst)
                return original
        except:
            lst.insert(index+1, '|')
            original=''.join(lst)
            return original
        try:
            if lst[index]=='×':
                lst.insert(index, '|')
                original=''.join(lst)
                return original
            else:
                lst.insert(index, '×')
        except:
            lst.insert(index, '×')
    elif new == '.':
        lst.insert(index, '.')
    elif new == '(':
        lst.insert(index, '(')
    elif new == ')':
        lst.insert(index, ')')
    elif new == 'π':
        lst.insert(index, 'π')
    elif new == 'X²':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^2')
    elif new == 'X³':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^3')
    elif new == 'Xˣ':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^')
    elif new == 'e':
        lst.insert(index, 'e')
    elif new == 'τ':
        lst.insert(index, 'τ')
    elif new == '000':
        lst.insert(index, '000')
    elif new == '√':
        lst.insert(index, '√()')
    lst.insert(index+1, '|')
    original=''.join(lst)
    return original
  

class math_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.buttons_one = [
            [
                Button(style=ButtonStyle.grey, label='1', id='1'),
                Button(style=ButtonStyle.grey, label='2', id='2'),
                Button(style=ButtonStyle.grey, label='3', id='3'),
                Button(style=ButtonStyle.blue, label='×', id='×'),
                Button(style=ButtonStyle.red, label='Exit', id='Exit')
            ],
            [
                Button(style=ButtonStyle.grey, label='4', id='4'),
                Button(style=ButtonStyle.grey, label='5', id='5'),
                Button(style=ButtonStyle.grey, label='6', id='6'),
                Button(style=ButtonStyle.blue, label='÷', id='÷'),
                Button(style=ButtonStyle.red, label='⌫', id='⌫')
            ],
            [
                Button(style=ButtonStyle.grey, label='7', id='7'),
                Button(style=ButtonStyle.grey, label='8', id='8'),
                Button(style=ButtonStyle.grey, label='9', id='9'),
                Button(style=ButtonStyle.blue, label='+', id='+'),
                Button(style=ButtonStyle.red, label='Clear', id='Clear')
            ],
            [
                Button(style=ButtonStyle.grey, label='00', id='00'),
                Button(style=ButtonStyle.grey, label='0', id='0'),
                Button(style=ButtonStyle.grey, label='.', id='.'),
                Button(style=ButtonStyle.blue, label='-', id='-'),
                Button(style=ButtonStyle.green, label='=', id='=')
            ],
            [
                Button(style=ButtonStyle.green, label='❮', id='❮'),
                Button(style=ButtonStyle.green, label='❯', id='❯'),
                Button(style=ButtonStyle.grey,
                       label='Change to scientific mode',
                       emoji='\U0001f9d1\u200D\U0001f52c',
                       id='400')
            ],
        ]
        self.buttons_two = [
            [
                Button(style=ButtonStyle.grey, label='(', id='('),
                Button(style=ButtonStyle.grey, label=')', id=')'),
                Button(style=ButtonStyle.grey, label='π', id='π'),
                Button(style=ButtonStyle.blue, label='×', id='×'),
                Button(style=ButtonStyle.red, label='Exit', id='Exit')
            ],
            [
                Button(style=ButtonStyle.grey, label='X²', disabled=True),
                Button(style=ButtonStyle.grey, label='X³', disabled=True),
                Button(style=ButtonStyle.grey, label='Xˣ', disabled=True),
                Button(style=ButtonStyle.blue, label='÷', id='÷'),
                Button(style=ButtonStyle.red, label='⌫', id='⌫')
            ],
            [
                Button(style=ButtonStyle.grey, label='e', id='e'),
                Button(style=ButtonStyle.grey, label='τ', id='τ'),
                Button(style=ButtonStyle.grey, label='000', id='000'),
                Button(style=ButtonStyle.blue, label='+', id='+'),
                Button(style=ButtonStyle.red, label='Clear', id='Clear')
            ],
            [
                Button(style=ButtonStyle.grey, label='√', id='√'),
                Button(style=ButtonStyle.grey, label=' ', disabled=True),
                Button(style=ButtonStyle.grey, label=' ', disabled=True),
                Button(style=ButtonStyle.blue, label='-', id='-'),
                Button(style=ButtonStyle.green, label='=', id='=')
            ],
            [
                Button(style=ButtonStyle.green, label='❮', id='❮'),
                Button(style=ButtonStyle.green, label='❯', id='❯'),
                Button(style=ButtonStyle.grey,
                       label='Change to normal modeㅤ',
                       emoji='\U0001f468\u200D\U0001f3eb',
                       id='401')
            ],
        ]

    @commands.command(aliases=['calc', 'calculator'])
    async def calcu(self, ctx):
        affichage = '|'
        id = 1
        e = discord.Embed(title=f'{ctx.author}\'s calculator',
                          description=f'```{affichage}```',
                          color=int("2f3136", 16))
       
        expression = ''
        m = await ctx.send(components=self.buttons_one, embed=e)

        def checkUp(res):
            return res.user.id == ctx.author.id and res.channel.id == ctx.channel.id and res.message.id == m.id

        while True:
            try:
                res = await self.bot.wait_for('button_click',
                                                 check=checkUp,
                                                 timeout=60)
            except asyncio.TimeoutError:
                a = discord.Embed(title=f'{ctx.author}\'s calculator',
                                  description=f'```{affichage}```',
                                  color=int("2f3136", 16))
           
                return await m.edit(embed=a)
            else:
                if str(res.author) == str(
                        res.message.embeds[0].title.split("'s calculator")[0]):
                    if res.component.id == 'Exit':
                        q = discord.Embed(
                            title=f'{ctx.author}\'s calculator',
                            description=f'{res.message.embeds[0].description}',
                            color=int("2f3136", 16))
                        return await res.respond(embed=q,
                                                 components=[],
                                                 type=7)
                    elif res.component.id == '⌫':
                        lst = list(res.message.embeds[0].description.replace(
                            '`', ''))
                        if len(lst) > 1:
                            try:
                                index = lst.index('|')
                                x = index - 2
                                y = index + 1
                                if lst[x] == '×' and lst[y] == '×':
                                    lst.pop(index - 1)
                                    lst.pop(index - 2)
                                else:
                                    lst.pop(index - 1)
                            except:
                                lst = ['|']
                        affichage = ''.join(lst)
                        expression = affichage
                    elif res.component.id == 'Clear':
                        expression = ''
                        affichage = '|'
                    elif res.component.id == '=':
                        if 'Syntax Error!' in affichage or affichage == '|':
                            expression = ''
                            affichage = '|'
                        else:
                            expression = expression.replace('|', '')
                            expression = calculate(expression)
                            affichage = f"{affichage.replace('|','')}={expression}"
                            expression = ''
                    elif res.component.id == '❮':
                        lst = list(res.message.embeds[0].description.replace(
                            '`', ''))
                        if len(lst) > 1:
                            try:
                                index = lst.index('|')
                                lst.remove('|')
                                lst.insert(index - 1, '|')
                            except:
                                lst = ['|']
                        affichage = ''.join(lst)
                    elif res.component.id == '❯':
                        lst = list(res.message.embeds[0].description.replace(
                            '`', ''))
                        if len(lst) > 1:
                            try:
                                index = lst.index('|')
                                lst.remove('|')
                                lst.insert(index + 1, '|')
                            except:
                                lst = ['|']
                        affichage = ''.join(lst)
                    elif res.component.id == '400':
                        id = 2
                        e = discord.Embed(title=f'{ctx.author}\'s calculator',
                                          description=f'```{affichage}```',
                                          color=int("2f3136", 16))
                 
                        await res.respond(embed=e,
                                          components=self.buttons_two,
                                          type=7)
                    elif res.component.id == '401':
                        id = 1
                        e = discord.Embed(title=f'{ctx.author}\'s calculator',
                                          description=f'```{affichage}```',
                                          color=int("2f3136", 16))
                     
                        await res.respond(embed=e,
                                          components=self.buttons_one,
                                          type=7)
                    else:
                        if '=' in affichage:
                            affichage = ''
                        expression = input_formatter(original=affichage,
                                                     new=res.component.label)
                        affichage = expression
                    if res.component.id != '400' and res.component.id != '401':
                        e = discord.Embed(title=f'{ctx.author}\'s calculator',
                                          description=f'```{affichage}```',
                                          color=int("2f3136", 16))
                       
                        if id == 1:
                            await res.respond(embed=e,
                                              components=self.buttons_one,
                                              type=7)
                        else:
                            await res.respond(embed=e,
                                              components=self.buttons_two,
                                              type=7)
#parabola

    @commands.command()
    @commands.guild_only()
    async def parabola(self, ctx, a: int, b: int, c: int):
        x = np.linspace(-10, 10, 1000)
        fig, ax = plt.subplots()
        y = a * x**2 + b * x + c
        ax.plot(x, y, 'g', label=f'y={a}x²+{b}x+{c}')
        plt.legend(loc='upper left')

        plt.grid()
        plt.savefig("foo.png")
        await ctx.send(file=discord.File("foo.png"))
        os.remove("foo.png")

#linear

    @commands.command()
    @commands.guild_only()
    async def linear(self, ctx, a: int, b: int):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        x = np.linspace(-5, 5, 100)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, a * x + b, '-r', label=f"y={a}x+{b}")
        plt.legend(loc='upper left')

        plt.grid()
        plt.savefig("foo2.png")
        await ctx.send(file=discord.File("foo2.png"))
        os.remove("foo2.png")


#cubic

    @commands.command()
    @commands.guild_only()
    async def cubic(self, ctx, a: int):
        x = np.linspace(-np.pi, np.pi, 100)
        y = np.sin(x)
        z = np.cos(x)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, y * a, 'c', label=f'y={a}sin(x)')
        plt.plot(x, z * a, 'm', label=f'y={a}cos(x)')
        plt.legend(loc='upper left')

        plt.grid()
        plt.savefig("foo3.png")
        await ctx.send(file=discord.File("foo3.png"))
        os.remove("foo3.png")


def setup(bot):
    bot.add_cog(math_fun(bot))
