import discord
from discord.ext import commands

TOKEN = 'типо токен'
PREFIX = '/'

admin_roles = [1107669935087431801, 1107669885317824513, 1107298355614339122]




intents = discord.Intents.all()
intents.members = True
bot = discord.Bot(command_prefix = PREFIX, intents = intents)



@bot.event
async def on_ready():
    print('Бот подключен!')
    await bot.change_presence(activity=discord.Game(name=f'{PREFIX}help'))


@bot.slash_command(name='ping',
                   description='Отправляет пинг!')
async def ping(inter):
    ping = bot.latency
    ping = round(ping, 2)
    embed = discord.Embed(
        title='Понг!:ping_pong:',
        description=f'Пинг: `{ping*1000} mc`',
        color=discord.Colour.green()
    )
    await inter.response.send_message(embed=embed)

@bot.slash_command(name='help',
                   description='Выводит список команд')
async def help(inter):
    embed_home = discord.Embed(
        title='Доступные команды',
        description='Все доступные команды видны в `/`, и недоступные тоже xD',
        color=discord.Colour.green()
    )
    await inter.response.send_message(embed=embed_home)

@bot.slash_command(name='kick',
                   description='Кикает с сервера указанного пользователя',
                   )
@commands.has_permissions(administrator = True)
async def kick(
    inter,
    member: Option(discord.member, description='Пользователь, которого наказывают.', required=True),
    reason: Option(str, description='Причина кика пользователя', required=False)
               ):
    embed = discord.Embed(title=f'Пользователь `{member}` был кикнут',
                          color=discord.Colour.green()
                          )
    if reason != None:
        embed.set_footer(text='По причине {reason}')
    
    await inter.response.send_message(embed=embed)
    

bot.run(TOKEN)