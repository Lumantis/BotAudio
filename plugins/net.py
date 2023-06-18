import discord
from discord.ext import commands

class Net(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='net')
    @commands.has_permissions(manage_messages=True)  # Seuls les utilisateurs avec la permission de gérer les messages peuvent utiliser cette commande
    async def net(self, ctx):
        await ctx.channel.purge(limit=None)

def setup(bot):
    bot.add_cog(Net(bot))
