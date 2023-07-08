import discord, os, asyncio, secrets
from   discord.ext import commands  

TOKEN = ""
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("We are online!")
    channel = bot.get_channel(1030550945962139760)
    randomIntros = ["Guess who's back!", "I'm alive!", "Y'all have been waiting for me, haven't you?", "Hello humans! I'm back."]
    await channel.send(secrets.choice(randomIntros))

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
