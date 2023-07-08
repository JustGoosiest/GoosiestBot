import discord
from discord.ext import commands


class Help(commands.Cog):

    @commands.command()
    async def help(self, ctx):
        await ctx.send("**Help**")

async def setup(bot):
    await bot.add_cog(Help(bot))
