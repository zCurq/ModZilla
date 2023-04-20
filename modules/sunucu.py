import datetime
import nextcord
from nextcord.ext import commands

class sunucu(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="sunucu",description="Sunucu bilgilerini görüntüler.")
    async def sunucu(self,interaction:nextcord.Interaction):
        x = nextcord.Embed(
            title=interaction.guild.name,
            timestamp=datetime.datetime.utcnow())

        try:
            x.set_thumbnail(url=interaction.guild.icon.url)
        except:
            pass

        metin_kanal = len([m for m in interaction.guild.channels if str(m.type) == "text"])
        ses_kanal = len([m for m in interaction.guild.channels if str(m.type) == "voice"])
        roller = len([m for m in interaction.guild.roles])

        tac = "<a:tac_ac:1096519555351859261>"

        x.add_field(name=f"{tac} **Kurucu**",value=interaction.guild.owner.mention)
        x.add_field(name=":id: **Sunucu ID'si**",value=interaction.guild.id)
        x.add_field(name=":speech_balloon: **Kanallar**",value=f"**{metin_kanal}** Yazılı | **{ses_kanal}** Sesli")
        x.add_field(name=f":busts_in_silhouette: **Üyeler**",value=f"**Toplam Üye** {str(len([m for m in interaction.guild.members if not m.bot]))}\n{str(interaction.guild.premium_subscription_count)} **Takviye** :sparkles:")
        x.add_field(name=":calendar: **Kuruluş Zamanı**",value=interaction.guild.created_at.strftime('**Tarih:** %d/%m/%Y \n**Saat:** %H:%M:%S %p'))
        x.add_field(name=f":closed_lock_with_key:  Roller (**{str(roller)}**)",value="** **",inline=False)

        await interaction.send(embed=x)
def setup(bot):
    bot.add_cog(sunucu(bot))