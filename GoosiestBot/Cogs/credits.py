import discord
from discord.ext import commands


class credits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        await ctx.send("JustGoosiest is my master.")


def setup(bot):
    bot.add_cog(credits(bot))
