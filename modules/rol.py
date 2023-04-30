import nextcord
from nextcord.ext import commands

class rol(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @nextcord.slash_command(name="rolver",description="Belirtilen kullanıcıya istenilen rolü verir.")
    async def rolver(self,interaction:nextcord.Interaction,üye:nextcord.Member,rol:nextcord.Role = nextcord.SlashOption(required=True)):
        if interaction.user.guild_permissions.manage_roles:
            if not üye.bot:
                if not rol in üye.roles:
                    try:
                        await üye.add_roles(rol)

                        x = nextcord.Embed(
                            title=f"{üye.display_name} kullanıcısı başarı ile güncellendi !",
                            colour=nextcord.Color.purple())
                        
                        x.add_field(name="Verilen Rol",value=f"<@&{rol.id}>")
                        x.add_field(name="Rolü Veren Yetkili",value=interaction.user.mention)

                        await interaction.send(embed=x)
                    except:
                        await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)
                else:
                    xy = nextcord.Embed(
                        title="Bir hata meydana geldi.",
                        description="*Kullanıcı zaten bu role sahip*",
                        colour=nextcord.Color.purple())
                    
                    await interaction.send(embed=xy)
            else:

                x = nextcord.Embed(
                    title="Rolver sistemi botlar için kapalıdır.",
                    description="*Botlara rol verirken yaşanan sık hatalar sebebi ile botlara rol verme kapalıdır.*",
                    colour=nextcord.Color.purple())
                
                await interaction.send(embed=x,ephemeral=True)
        else:
            await interaction.send("Bu komutu kullanabilmek için `Rolleri yönet` yetkisine sahip olmalısın.")       

    @nextcord.slash_command(name="rolal",description="Belirtilen kullanıcıdan belirtilen rolü alır.")
    async def rolal(self,interaction:nextcord.Interaction,üye:nextcord.Member,rol:nextcord.Role = nextcord.SlashOption(required=True)):
        
        if interaction.user.guild_permissions.manage_roles:
            if not üye.bot:

                if rol in üye.roles:
                    try:
                        
                        await üye.remove_roles(rol)

                        x = nextcord.Embed(
                            title=f"{üye.display_name} kullanıcısı başarı ile güncellendi !",
                            colour=nextcord.Color.purple())
                        
                        x.add_field(name="Alınan Rol",value=f"<@&{rol.id}>")
                        x.add_field(name="Rolü Alan Yetkili",value=interaction.user.mention)

                        await interaction.send(embed=x)
                    except:
                        await interaction.send(":pensive: **İşlem başarısız**\n> Bu komutu kullanabilmek için gerekli yetkiye sahip olmayabilirsin.\n> Bu komutu kullanmak için bota gerekli yetkiler verilmemiş olabilir.",ephemeral=True)
                else:
                    xy = nextcord.Embed(
                        title="Bir hata meydana geldi.",
                        description="*Kullanıcı zaten bu role sahip değil.*",
                        colour=nextcord.Color.purple()) 
                    
                    await interaction.send(embed=xy)
            else:

                x = nextcord.Embed(
                    title="Rol al sistemi botlar için kapalıdır.",
                    description="*Botlardan rol alırken yaşanan sık hatalar sebebi ile botlardan rol alma kapalıdır.*",
                    colour=nextcord.Color.purple())
                    
                await interaction.send(embed=x,ephemeral=True)  
        else:
            await interaction.send("Bu komutu kullanabilmek için `Rolleri yönet` yetkisine sahip olmalısın.")       

def setup(bot):
    bot.add_cog(rol(bot))