import discord
from discord.ext import commands
import token
import os

TOKEN = ""
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print("We are online!")

# load cogs
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')


bot.run(TOKEN)
