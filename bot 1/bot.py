import discord
from discord.ext import commands
import random
import os
# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix="$",intents=intents)
memes1 = os.listdir ("./reread/programing")
animals = {"rihno":"Africa","emperuir_penguin":"Antartica","lion":"India","flamingo":"Caucasus"}
water = {"Africa":"Libya, Algeria and Chad","India":"Puri","Usa":"Kentucky,Atlanta and Calarado"}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send("hi")
@bot.command()
async def habitat_zone(ctx, animal=""):
    if animal in animals:
        await ctx.send(animals[animal])
    else:
        await ctx.send("we dont have that word")
@bot.command() 
async def clear_water(ctx, states=""):
    if states in water:
        await ctx.send(water[states])
    else:
        await ctx.send("we dont have that country")
@bot.command()
async def repeat(ctx, word="",count=1):
    if word=="":
        await ctx.send("send a word")
    else: 
        await ctx.send((word+" ")*count)


@bot.command()
async def calculator(ctx, number1=0,eqations="",number2=0):
    if eqations=="+":
        await ctx.send(number1+number2)
    elif eqations=="-":
        await ctx.send(number1-number2)
    elif eqations=="*":
        await ctx.send(number1*number2)
    elif eqations=="/": 
        if number2==0:
            await ctx.send("division by zero")
        else:
            
            await ctx.send(number1/number2)
    else:
        await ctx.send("words is not in use")

@bot.command()
async def mem(ctx, catigories=""):
    if catigories=="":
        await ctx.send("say catigories")
    elif catigories=="programing":
        with open(f"./reread/programing/{random.choice(memes1)}","rb") as f:
            image = discord.File(f)
        await ctx.send(file = image)
    
    

    

    
bot.run()

