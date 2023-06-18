from discord.ext import commands

class Plugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calculer(self, ctx, *, equation):
        try:
            result = eval(equation)
            await ctx.send(f"Résultat : {result}")
        except Exception as e:
            await ctx.send(f"Erreur : {str(e)}")
