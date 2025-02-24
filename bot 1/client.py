import discord


# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else: 
        await message.channel.send("i dont understand")
client.run("MTMzNjA3OTI3MTk5MDUyNTk2Mg.Gyddu8.Ow4gtGQHFUqtcMn9mqC2Wxe0Gdl1t5nW_Tihl8")