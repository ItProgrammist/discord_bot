import conf
import discord

client = discord.Client()




@client.event # Функция сработает только в тот момент, когда на неё придёт запрос
async def on_message(message):
    # Проверка на дурака №1 - Отправитель является самим ботом
    if message.author.bot:
        return
    # Проверка на дурака №2 - Отправитель является другим ботом
    if 

    if message.author == client.user:
        # Изначально сообщение пустое

    if message.channel.id == 825340703084118046:
        print(message)
        # Ответить пользователю в формате "hello, {user.name} - your message {user.}"
        msg = None
        #Отправляем сообщение в канал channel

        # 1. /hello - просто сообщение
        # 2. /about_me - сообщение пользователю по его параметру id/name (если есть ник, то добавить "твой ник nick")
        # 3. /repeat [] - повторить за пользователем
        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name}'

        elif message.content == "/about_me":
            await bot.say("{} is your name".format(message.author.id))
        
        # Отправляем сообщение, если оно есть
        if  msg != None:
            await message.channel.send(msg)





client.run(conf.bot_token)



