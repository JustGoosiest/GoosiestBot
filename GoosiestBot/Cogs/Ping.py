import discord
from discord.ext import commands

class Ping(commands.Cog):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'_{ctx.message.author.mention} PONG!_')

async def setup(bot):
    await bot.add_cog(Ping(bot))
