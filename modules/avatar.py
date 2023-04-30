import nextcord
from nextcord.ext import commands
from nextcord import SlashOption

class avatar(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="avatar",description="Belirtilen üyenin avatarını alırsınız.")
    async def avatar(self,interaction:nextcord.Interaction,üye:nextcord.Member):

        try:
            x = nextcord.Embed(
                title=f"İndirmek için bana tıkla !",
                colour=nextcord.Color.purple(),
                url=üye.avatar.url)
            
            x.set_image(url=üye.avatar.url)

            await interaction.send(embed=x)
        except:
            await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)

def setup(bot):
    bot.add_cog(avatar(bot))