import discord
from discord.ext import commands
import time, datetime

class Uptime(commands.Cog):

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    #create a command in the cog
    @commands.command()
    async def uptime(self,ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

async def setup(bot):
    await bot.add_cog(Uptime(bot))