import datetime
import nextcord , sqlite3
from nextcord.ext import commands

class otorol(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="otorol",description="Sunucuya katılanlara otomatik rol verir.")
    async def otorol(self,interaction:nextcord.Interaction,rol:nextcord.Role = nextcord.SlashOption(required=True)):
        if interaction.user.guild_permissions.administrator:
            with sqlite3.connect("veritabanı.db") as veritabanı:
                imleç = veritabanı.cursor()
                imleç.execute("CREATE TABLE IF NOT EXISTS otorol(sunucu_id INT,rol INT,yetkili_id INT,tarih TEXT)")
                imleç.execute(f"SELECT * FROM otorol WHERE (sunucu_id={interaction.guild.id})")
                veri = imleç.fetchone()
                
                if veri:
                    x = nextcord.Embed(
                        title="Otorol sistemi bu sunucu için zaten aktif.",
                        colour=nextcord.Color.purple())
                        
                    x.add_field(name="Verilecek Rol",value=f"<@&{veri[1]}>")
                    x.add_field(name="Sistemi kuran yetkili",value=f"<@{veri[2]}>")
                    x.add_field(name="Sistemin kurulma tarihi",value=f"`{veri[3][:-7]}`")

                    await interaction.send(embed=x)
                else:
                    imleç.execute("INSERT INTO otorol(sunucu_id,rol,yetkili_id,tarih) VALUES (?,?,?,?)",(interaction.guild.id,rol.id,interaction.user.id,datetime.datetime.now()))

                    x = nextcord.Embed(
                        title="Otorol sistemi aktif edildi.",
                        colour=nextcord.Color.purple()
                    )
                    try:x.set_thumbnail(url=interaction.guild.icon.url())
                    except:pass

                    tarih = datetime.datetime.now()
                    x.add_field(name="Sistemi Aktif Eden Yetkili",value=interaction.user.mention)
                    x.add_field(name="Sistemin Kurulma Tarihi",value=f"`{str(tarih)[:-7]}`")
                    x.add_field(name="Verilecek Rol",value=f"<@&{rol.id}>")

                    await interaction.send(embed=x)
        else:
            await interaction.send("Bu komutu kullanabilmek için `Yönetici` yetkisine sahip olmalısınız.")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        if not member.bot:
            with sqlite3.connect("veritabanı.db") as veritabanı:
                imleç = veritabanı.cursor()
                imleç.execute(f"SELECT * FROM otorol WHERE (sunucu_id={member.guild.id})")
                veri = imleç.fetchone()

                if veri:
                    sunucu = member.guild
                    rol = nextcord.utils.get(sunucu.roles,id=veri[1])

                    await member.add_roles(rol)
                

def setup(bot):
    bot.add_cog(otorol(bot))