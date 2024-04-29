# All Imports As Needed
import requests
import datetime
import colorama
import discord
import os
from discord.ext import commands
import asyncio
import json


# Gets Your Prefix And Discord Bot Token From A Config.json File
with open('./config.json', 'r') as f:
    config = json.load(f)
    TOKEN = config['TOKEN']
    PREFIX = config['PREFIX']




# Class Of The Bot
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=discord.Intents.all()
        )
        
    async def setup_hook(self):
        cog_dir = "./cogs"
        for folder in os.listdir(cog_dir):
         full_path = os.path.join(cog_dir, folder)
         black_listed_files = ["channel.txt"]
         if os.path.isdir(full_path):
           for file in os.listdir(full_path):
            if file.endswith(".py") and file[:-3] not in black_listed_files:
              cog_path = f"cogs.{folder}.{file[:-3]}"
              await self.load_extension(cog_path)
        
# Runs The Bot Itself
Bot().run(TOKEN)
