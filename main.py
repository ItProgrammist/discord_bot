import conf
import discord
from discord.ext import commands

# # Настраиваем расширенный доступ Intents
# intense = discord.Intents.default()
# intense.members = True

# # Создаём подключение бота
# client = discord.Client(intents=intense)


# id_channel = 825340703084118046

# @client.event
# async def on_message(message):
#     # <Message 
#     # id=825337927005110293 
#     # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#     # type=<MessageType.default: 0> 
#     # author=<Member id=635376536761139211 name='Ulan' discriminator='9113' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
#     # flags=<MessageFlags value=0>>

#     # Проверка на дурака №1 - Отправлятор является самим ботом
#     if message.author == client.user:
#         return
    
#     # Проверка на дурака №2 - Отправлятор является другим ботом
#     if message.author.bot:
#         return

#     # задаём каналы для бота [Канал General]
#     global id_channel
#     if message.channel.id == id_channel:
#         # Изначально, сообщение пустое
#         msg = None
        
#         # Контекс, разбивающийся на два эл-а списка (команду /... и 'само сообщение')
#         ctx = message.content.split(" ", maxsplit = 1) # Максимальное количество

#         # 1. /hello - просто сообщение
#         if message.content == "/hello":
#             msg = f'Hello, {message.author.name}. I am {client.user.name}'

#         # 2. /about_me - сообщение пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")
#         elif message.content == "/about me":
#             msg = f'Hello, {message.author.name}, your id is: {message.author.id}'

#         # *3. /repeat [] - повторить за пользователем
#         elif ctx[0] == "/repeat":
#             msg = ctx[1]

#         #*4 /get_member
#         elif ctx[0] == "/get_member":
#             name = ctx[1]
#             if message.author.guild.name == 'Bots':
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     if ctx[1] == member.id or ctx[1] == member.name:
#                         msg = f'Есть такой: {member.name}, {member.id}'
#                         break
            
#                     else:
#                         msg = f'Такого пользователя нет, попробуйте ввести другие параметры.'

#         # *5 /get_members
#         elif ctx[0] == '/get_members':
#             msg = ""
#             if message.author.guild.name == 'Bots':
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""} - {member.id}\n'          

#         # *6 /get_channels
#         elif ctx[0] == "/get_channels":
#              msg = ""
#              if message.author.guild.name == 'Bots':
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     msg += f'{idx+1}. {channel.name} - {channel.id}\n'

#         # *7 /goto
#         elif ctx[0] == "/goto":
#             if message.author.guild.name == 'Bots':
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     if ctx[1] == channel.id or ctx[1] == channel.name:
#                         id_channel = ctx[1]
#                         break
#                     else:
#                         msg = f'Ошибка подключения к каналу. Пожалуйста, укажите правильное имя/id канала!'

#         # Отправляем сообщение если оно есть
#         if msg != None:
#             await message.channel.send(msg)





# client.run(conf.bot_token)


bot = commands.Bot(command_prefix= "!")

@bot.command(name = "hello") # Декоратор
async def command_hello(ctx, *args): # args = tuple (кортежи)
    message = " ".join(args)
    if ctx.channel.id == 825340703084118046:
        msg = f"Hello to you! You said: '{message}'"
        await ctx.channel.send(msg)

# 2. /about_me - сообщение пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")
@bot.command(name = "about_me")
async def command_about_me(ctx):
    msg = f'Hello, {ctx.author.name}, your id is: {ctx.author.id}'
    await ctx.channel.send(msg)

# *3. /repeat [] - повторить за пользователем
@bot.command(name="repeat")
async def command_repeat(ctx, *args):
    message = " ".join(args)
    msg = f'{message}'
    await ctx.channel.send(msg)


bot.run(conf.bot_token)