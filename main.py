import conf
import discord

# Настраиваем расширенный доступ Intents
intense = discord.Intents.default()
intense.members = True

# Создаём подключение бота
client = discord.Client(intents=intense)




@client.event
async def on_message(message):
    # <Message 
    # id=825337927005110293 
    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
    # type=<MessageType.default: 0> 
    # author=<Member id=635376536761139211 name='Ulan' discriminator='9113' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
    # flags=<MessageFlags value=0>>

    # Проверка на дурака №1 - Отправлятор является самим ботом
    if message.author == client.user:
        return
    
    # Проверка на дурака №2 - Отправлятор является другим ботом
    if message.author.bot:
        return

    # задаём каналы для бота [Канал General]
    if message.channel.id == 825340703084118046:
        # Изначально, сообщение пустое
        msg = None
        
        # Контекс, разбивающийся на два эл-а списка (команду /... и 'само сообщение')
        ctx = message.content.split(" ", maxsplit = 1) # Максимальное количество

        # 1. /hello - просто сообщение
        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name}'

        # 2. /about_me - сообщение пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")
        elif message.content == "/about me":
            msg = f'Hello, {message.author.name}, your id is: {message.author.id}'

        # *3. /repeat [] - повторить за пользователем
        elif ctx[0] == "/repeat":
            msg = ctx[1]

        #*4 /get_member
        # elif ctx[0] == "/get_member":
        #     name = ctx[1]
        #     if name == '':
        #         msg = f'Enter username, please!'
        #     elif 

        # *5 /get_members
        elif message.content == '/get_members':
            msg = ""
            if message.author.guild.name == 'Bots':
                for idx, member in list(enumerate(message.author.guild.members)):
                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""} - {member.id}\n'          
                        
        # Отправляем сообщение если оно есть
        if msg != None:
            await message.channel.send(msg)





client.run(conf.bot_token)