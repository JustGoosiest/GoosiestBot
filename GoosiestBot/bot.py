import discord, os, asyncio
from   discord.ext import commands

TOKEN = ""
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("We are online!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("That's not even a command. _yet._")


# load cogs
async def load():
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'Cogs.{filename[:-3]}')

asyncio.run(load())
bot.run(TOKEN)
