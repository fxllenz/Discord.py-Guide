import discord
from discord import app_commands
from discord.ext import commands

class Cogs_Example(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @commands.command()
  async def ping(ctx):
    await ctx.send('Pong! 🏓')


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Cogs_Example(bot))
