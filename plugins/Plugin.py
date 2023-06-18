from discord.ext import commands

class Plugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Insérer ici la logique de votre plugin
    # Par exemple, une commande "calculer" pourrait ressembler à ceci :

    @commands.command()
    async def calculer(self, ctx, *, equation):
        try:
            result = eval(equation)
            await ctx.send(f"Résultat : {result}")
        except Exception as e:
            await ctx.send(f"Erreur : {str(e)}")
