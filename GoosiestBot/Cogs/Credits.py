import discord
from discord.ext import commands


class Credits(commands.Cog):

    @commands.command()
    async def credits(self, ctx):
        embed=discord.Embed(title="JustGoosiest", url="https://github.com/JustGoosiest", description="JustGoosiest is my master.", color=0x66CDAA)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Credits(bot))