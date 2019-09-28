import discord
from discord.ext import commands
import game
import random
token = 'ENTER TOKEN'
sessions = {}
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def start(ctx):
    if not ctx.guild.id in sessions:
        sessions[ctx.guild.id] = game.Game(ctx)
        g = sessions[ctx.guild.id]
        await g.start(ctx)
    else:
        await ctx.send("There is already a game in this channel")
@bot.command()
async def join(ctx):
    g = sessions[ctx.guild.id]
    if g.state:
        await g.join(ctx)
    else:
        await ctx.send("There is already a game being played, please end the existing game")
@bot.command()
async def play(ctx):
    g = sessions[ctx.guild.id]
    if g.state:
        await g.play(ctx)
    else:
        await ctx.send("There is an existing game")
@bot.command()
async def end(ctx):
    sessions.pop(ctx.guild.id)
@bot.command()
async def h(ctx):
    await ctx.send("start, join, play, end, help, prefix=$")
bot.run(token)