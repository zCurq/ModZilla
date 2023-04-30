import nextcord , datetime
from nextcord.ext import commands

class yasakla(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="yasakla",description="Belirtilen üyeyi sunucudan yasaklar.")
    async def yasakla(self,interaction:nextcord.Interaction,üye:nextcord.Member = nextcord.SlashOption(required=True)):
        if interaction.user.guild_permissions.ban_members:
            konfeti = "<a:konfeti_ac:1096144555088281640>"
            moderasyon = "<a:mod_ac:1096145030281961623>"
            
            x = nextcord.Embed(
                title=f"{konfeti} {üye.name} sunucudan yasaklandı !",
                colour=nextcord.Color.purple()
            )

            x.add_field(name=f"{moderasyon} Yasaklayan yetkili:",value=interaction.user.mention,inline=True)
            x.add_field(name=":bell: Yasaklanma tarihi:",value=nextcord.utils.format_dt(datetime.datetime.now(),style="R"))
            x.set_thumbnail(url=self.bot.user.avatar.url)

            try:
                await üye.ban(reason=None)
                await interaction.response.send_message(embed=x,ephemeral=False)
            except:
                await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)
        else:
            await interaction.send("Bu komutu kullanabilmek için `Üyeleri Yasakla` yetkisine sahip olmalısın.")

def setup(bot):
    bot.add_cog(yasakla(bot))