import disnake
from disnake.ext import commands

TOKEN = 'token'
PREFIX = '/'

admin_roles = [1107669935087431801, 1107669885317824513, 1107298355614339122]

intents = disnake.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    print('Бот подключен!')
    await bot.change_presence(activity=disnake.Game(name=f'{PREFIX}help'))


@bot.slash_command(name='ping',
                   description='Отправляет пинг!')
async def ping(inter):
    ping_ms = round(bot.latency, 2) * 1000
    embed = disnake.Embed(
        title='Понг! :ping_pong:',
        description=f'Пинг: `{ping_ms} ms`',
        color=disnake.Colour.green()
    )
    await inter.response.send_message(embed=embed)


@bot.slash_command(name='help',
                   description='Выводит список команд')
async def help_cmd(inter):
    embed_home = disnake.Embed(
        title='Доступные команды',
        description='Все доступные команды видны в `/` и недоступные тоже xD',
        color=disnake.Colour.green()
    )
    await inter.response.send_message(embed=embed_home)


bot.run(TOKEN)
