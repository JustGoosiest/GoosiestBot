import discord
from discord.ext import commands


class Clear(commands.Cog):


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, limit: str = None):

        try:
            limit = int(limit)
        except ValueError:
            await ctx.send(f"_{limit} is not a valid number._")
            return
        
        if limit <= 0:
            await ctx.send("_You can't clear nothing._")
            return
        
        try:
            await ctx.channel.purge(limit=limit + 1)
            await ctx.send(f"_{limit} messages have been cleared succesfully!_")
        except discord.Forbidden:
            await ctx.send("I don't have permission to clear messages.")
        except discord.HTTPException:
            await ctx.send("Failed to clear messages.")



#    @commands.command()
#    async def clear(ctx, amount=int):
#        if amount <= 0:
#            await ctx.send("_You can't delete nothing._")
#            return
#        else:
#            await ctx.channel.purge(limit=amount)


async def setup(bot):
    await bot.add_cog(Clear(bot))