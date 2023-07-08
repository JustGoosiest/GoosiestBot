# https://discord.com/api/oauth2/authorize?client_id=1126573919869079754&permissions=8&scope=bot

import discord
from discord.ext import commands


class Invite(commands.Cog):

    @commands.command()
    async def invite(self, ctx):
        link = "Invite me to your server :" + "\n" + "**https://discord.com/api/oauth2/authorize?client_id=1126573919869079754&permissions=8&scope=bot**"
        await ctx.send(link)

async def setup(bot):
    await bot.add_cog(Invite(bot))