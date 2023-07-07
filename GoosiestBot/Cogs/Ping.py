import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("_PONG!_")


def setup(bot):
    bot.add_cog(Ping(bot))