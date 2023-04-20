import nextcord , os , colorama, sys
from dotenv import load_dotenv, find_dotenv
from nextcord.ext import commands

sys.dont_write_bytecode = True #__pycache__ klasörünü kaldırır.
load_dotenv(find_dotenv())

bot = commands.Bot(help_command=None,intents=nextcord.Intents.all(),status=nextcord.Status.idle,activity=nextcord.Game("Sunucular ile ilgileniyor."))

for modules in os.listdir("./modules"):
    if modules.endswith(".py"):
        bot.load_extension(f"modules.{modules[:-3]}")

@bot.event
async def on_ready():
    print(colorama.Back.GREEN + f"{bot.user} olarak giriş yaptım." + colorama.Back.RESET)

bot.run(os.environ.get("token")) 