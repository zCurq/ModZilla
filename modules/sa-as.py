import nextcord , datetime
import sqlite3 as sql
from nextcord.ext import commands

class sa_as(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="selamlama_aç",description="Selamlama sistemini açar.")
    async def selamlama_aç(self,interaction:nextcord.Interaction):

        if interaction.user.guild_permissions.manage_messages:
            with sql.connect("veritabanı.db") as veritabanı:
                imleç = veritabanı.cursor()
                imleç.execute("CREATE TABLE IF NOT EXISTS selamla(sunucu_id INT,yetkili_id TEXT,tarih TEXT)")
                imleç.execute(f"SELECT * FROM selamla WHERE (sunucu_id={interaction.guild.id})")
                veri = imleç.fetchone()

                if veri:
                    x = nextcord.Embed(
                        title="Selamlama sistemi bu sunucu için zaten aktif",
                        colour=nextcord.Color.purple())
                    
                    x.add_field(name="Sistemi kuran yetkili",value=f"`{veri[1]}`")
                    x.add_field(name="Sistemin kurulma tarihi",value=f"`{veri[2][:-7]}`")

                    await interaction.send(embed=x)

                else:
                    imleç.execute("INSERT INTO selamla(sunucu_id,yetkili_id,tarih) VALUES (?,?,?)",(interaction.guild.id,str(interaction.user),datetime.datetime.now()))

                    x = nextcord.Embed(
                        title="Selamlama sistemi bu sunucu için aktif edildi.",
                        colour=nextcord.Color.purple())
                    
                    x.add_field(name="Sistemi kuran yetkili",value=interaction.user.mention)
                    x.add_field(name="Sistemin kurulma tarihi",value=nextcord.utils.format_dt(datetime.datetime.now(),style="F"))

                    await interaction.send(embed=x)
        else:
            await interaction.send("Bu komutu kullanabilmek için `Mesajları Yönet` yetkisine sahip olmalısın.",ephemeral=True)
            
    @nextcord.slash_command(name="selamlama_kapat",description="Selamlama sistemini kapatır.")
    async def selamlama_kapat(self,interaction:nextcord.Interaction):

        if interaction.user.guild_permissions.manage_messages:
            with sql.connect("veritabanı.db") as veritabanı:
                imleç = veritabanı.cursor()
                imleç.execute("CREATE TABLE IF NOT EXISTS selamla(sunucu_id INT)")
                imleç.execute(f"SELECT * FROM selamla WHERE (sunucu_id={interaction.guild.id})")
                veri = imleç.fetchone()

                if not veri:
                    x = nextcord.Embed(
                        title="Selamlama sistemi bu sunucu için zaten kapalı",
                        colour=nextcord.Color.purple())

                    await interaction.send(embed=x)

                else:
                    imleç.execute(f"DELETE FROM selamla WHERE sunucu_id={interaction.guild.id}")
                    x = nextcord.Embed(
                        title="Selamlama sistemi bu sunucu için kapatıldı.",
                        colour=nextcord.Color.purple())
                    
                    await interaction.send(embed=x)
        else:
            await interaction.send("Bu komutu kullanabilmek için `Mesajları Yönet` yetkisine sahip olmalısın.",ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author.bot:
            with sql.connect("veritabanı.db") as veritabanı:
                imleç = veritabanı.cursor()
                imleç.execute(f"SELECT * FROM selamla WHERE (sunucu_id={message.guild.id})")
                veri = imleç.fetchone()

                if veri:

                    if message.content.lower() == "sa" or message.content.lower() == "selamın aleyküm":
                        await message.channel.send(f"Aleyküm Selam {message.author.mention}")
        
        

def setup(bot):
    bot.add_cog(sa_as(bot))