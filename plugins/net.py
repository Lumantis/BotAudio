import discord
from discord.ext import commands
import warnings

class Net(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='net')
    @commands.has_permissions(manage_messages=True)
    async def clear_channel(self, ctx):
        await ctx.channel.purge(limit=None)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.bot.user and not after.channel:
            shutil.rmtree('playlist')
            os.mkdir('playlist')

def setup(bot):
    bot.add_cog(Net(bot))