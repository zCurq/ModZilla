import nextcord , datetime
from nextcord.ext import commands

class temizle(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="temizle",description="İstenilen sayıda mesajı siler.")
    async def temizle(self,interaction:nextcord.Interaction,adet:int = nextcord.SlashOption(required=True)):

        try:
            await interaction.channel.purge(limit=adet)

            x = nextcord.Embed(
                title=f"*{str(adet)}* adet mesaj silindi !",
                colour=nextcord.Color.purple())
            
            x.add_field(name="Mesajları silen yetkili",value=interaction.user.mention)
            x.add_field(name="Mesajların temizlenme tarihi",value=nextcord.utils.format_dt(datetime.datetime.now(),style="R"))

            await interaction.send(embed=x)

        except:
            await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)

def setup(bot):
    bot.add_cog(temizle(bot))
