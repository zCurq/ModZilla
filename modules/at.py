import nextcord , datetime
from nextcord.ext import commands

class at(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="at",description="Belirtilen üyeyi sunucudan atar.")
    async def at(self,interaction:nextcord.Interaction,üye:nextcord.Member = nextcord.SlashOption(required=True)):

        if interaction.user.guild_permissions.kick_members:
            konfeti = "<a:konfeti_ac:1096144555088281640>"
            moderasyon = "<a:mod_ac:1096145030281961623>"
            
            x = nextcord.Embed(
                title=f"{konfeti} {üye.name} sunucudan atıldı !",
                colour=nextcord.Color.purple()
            )

            x.add_field(name=f"{moderasyon} atyan yetkili:",value=interaction.user.mention,inline=True)
            x.add_field(name=":bell: atnma tarihi:",value=datetime.datetime.utcnow())
            x.set_thumbnail(url=self.bot.user.avatar.url)

            try:
                await üye.kick(reason=None)
                await interaction.response.send_message(embed=x,ephemeral=False)
            except:
                await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)
        else:
            await interaction.send("Bu komutu kullanmak için `Üyeleri At` yetkisine sahip olmalısın.",ephemeral=False)

def setup(bot):
    bot.add_cog(at(bot))