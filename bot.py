# All The Imports Needed Here!

import discord
from discord.ext import commands

# Starting The Bot Instance
# Feel Free To Change Command Prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# When The Bot Is Ready, Print That Its Online
@bot.event
async def on_ready():
  print(f'{bot.user.name} Is Online')

# Simple Ping Command
@bot.command()
async def ping(ctx):
  await ctx.reply('Pong! 🏓')


# Put Your Bot Token In The ''
bot.run('YOUR TOKEN HERE')
