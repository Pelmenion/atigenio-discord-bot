import disnake
from disnake.ext import commands

TOKEN = 'MTEwODA4Njk5NTkyNzk2NTY5Ng.G1j_BB.au0AMSlWy4D3VxOlMGeek84-sfKGjXGtGAzlkA'
PREFIX = '/'

admin_roles = [1107669935087431801, 1107669885317824513, 1107298355614339122]


intents = disnake.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = PREFIX, intents = intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print('Бот подключен!')
    await bot.change_presence(activity=disnake.Game(name=f'{PREFIX}help'))