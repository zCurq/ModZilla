import nextcord
from nextcord.ext import commands

class yardım(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="yardım",description="Tüm komutları görüntüler")
    async def yardım(self,interaction:nextcord.Interaction):

        x = nextcord.Embed(
            title="ModZilla komutları",
            description="Tüm komutlar Slash( / ) komutlarını destekler. '/' yazarak komutlara bakabilirsiniz.",
            colour=nextcord.Color.purple())
        
        await interaction.send(embed=x)

def setup(bot):
    bot.add_cog(yardım(bot))