import nextcord
from nextcord.ext import commands

class nuke(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="nuke",description="Bulunduğun kanaldaki tüm mesajlari temizler.")
    async def nuke(self,interaction:nextcord.Interaction):

        if interaction.user.guild_permissions.manage_messages:
            try:
                await interaction.channel.purge()

                x = nextcord.Embed(
                    title="Tüm mesajlar temizlendi !",
                    color=nextcord.Colour.purple())
                
                await interaction.send(embed=x,ephemeral=True)
            except:
                pass
        else:
            await interaction.send("Bu komutu kullanabilmek için `Mesajları Yönet` yetkisine sahip değilsin.")

def setup(bot):
    bot.add_cog(nuke(bot))

        
