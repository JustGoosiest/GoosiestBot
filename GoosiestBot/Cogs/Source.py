import discord
from discord.ext import commands


class Source(commands.Cog):
    
    @commands.command()
    async def source(self, ctx):
        await ctx.send("**https://github.com/JustGoosiest/GoosiestBot**")

async def setup(bot):
    await bot.add_cog(Source(bot))