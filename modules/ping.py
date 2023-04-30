import nextcord
from nextcord.ext import commands

class ping(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="ping",description="Botun gecikmesini gösterir.")
    async def ping(self,interaction:nextcord.Interaction):

        ping = round(self.bot.latency * 1000)

        x = nextcord.Embed(
            title=f"*Botun gecikmesi:* **{str(ping)}ms!**",
            colour=nextcord.Color.purple())
        
        await interaction.send(embed=x,ephemeral=False)
        
def setup(bot):
    bot.add_cog(ping(bot))