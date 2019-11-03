import discord

from discord.ext import commands
from discord.ext.commands import Bot

import random as rand
import pyowm
import os

import json

owm = pyowm.OWM('2e8e40308212b73167bdd6a4c8dd3b32', language = "ru")

Bot = commands.Bot(command_prefix= "!")

cards21 = False

@Bot.event
async def on_ready():
    print("Мое уважение")
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на даунов"))


@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello {author.mention}")


@Bot.command(pass_context=True)
async def desktop(ctx):
    link = "https://discordapp.com/channels/" +str(ctx.message.guild.id)+ "/" + str(ctx.message.author.voice.channel.id)
    await ctx.send(link)
    await ctx.message.delete()

#send image
@Bot.command()
async def dota(ctx):
    await ctx.send(file=discord.File('images/dota.jpg'))
    await ctx.message.delete()


@Bot.command()
async def f(ctx):
    await ctx.send(file=discord.File('images/f.jpg'))
    await ctx.message.delete()

@Bot.command()
async def kote(ctx):
    await ctx.send(file=discord.File('images/kote.png'))
    await ctx.message.delete()

@Bot.command()
async def kredit(ctx):
    await ctx.send(file=discord.File('images/kredit.jpg'))
    await ctx.message.delete()

@Bot.command()
async def pika(ctx):
    await ctx.send(file=discord.File('images/pika.jpg'))
    await ctx.message.delete()


#21
@Bot.command()
async def cards_roll(ctx):
    z = rand.randint(1,4)
    if z == 1:
        x = rand.randint(1,13)
        if x == 1:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_001.jpg'))
        elif x == 2:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_002.jpg'))
        elif x == 3:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_003.jpg'))
        elif x == 4:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_004.jpg'))
        elif x == 5:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_005.jpg'))
        elif x == 6:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_006.jpg'))
        elif x == 7:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_007.jpg'))
        elif x == 8:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_008.jpg'))
        elif x == 9:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_009.jpg'))
        elif x == 10:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_010.jpg'))
        elif x == 11:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_011.jpg'))
        elif x == 12:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_012.jpg'))
        else:
            await ctx.author.send(file=discord.File('cards/clubs/image_part_013.jpg'))        
    elif z == 2:
        x = rand.randint(1,13)
        if x == 1:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_001.jpg'))
        elif x == 2:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_002.jpg'))
        elif x == 3:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_003.jpg'))
        elif x == 4:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_004.jpg'))
        elif x == 5:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_005.jpg'))
        elif x == 6:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_006.jpg'))
        elif x == 7:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_007.jpg'))
        elif x == 8:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_008.jpg'))
        elif x == 9:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_009.jpg'))
        elif x == 10:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_010.jpg'))
        elif x == 11:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_011.jpg'))
        elif x == 12:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_012.jpg'))
        else:
            await ctx.author.send(file=discord.File('cards/diamonds/image_part_013.jpg'))
    elif z == 3:
        x = rand.randint(1,13)
        if x == 1:
            await ctx.author.send(file=discord.File('cards/spades/image_part_001.jpg'))
        elif x == 2:
            await ctx.author.send(file=discord.File('cards/spades/image_part_002.jpg'))
        elif x == 3:
            await ctx.author.send(file=discord.File('cards/spades/image_part_003.jpg'))
        elif x == 4:
            await ctx.author.send(file=discord.File('cards/spades/image_part_004.jpg'))
        elif x == 5:
            await ctx.author.send(file=discord.File('cards/spades/image_part_005.jpg'))
        elif x == 6:
            await ctx.author.send(file=discord.File('cards/spades/image_part_006.jpg'))
        elif x == 7:
            await ctx.author.send(file=discord.File('cards/spades/image_part_007.jpg'))
        elif x == 8:
            await ctx.author.send(file=discord.File('cards/spades/image_part_008.jpg'))
        elif x == 9:
            await ctx.author.send(file=discord.File('cards/spades/image_part_009.jpg'))
        elif x == 10:
            await ctx.author.send(file=discord.File('cards/spades/image_part_010.jpg'))
        elif x == 11:
            await ctx.author.send(file=discord.File('cards/spades/image_part_011.jpg'))
        elif x == 12:
            await ctx.author.send(file=discord.File('cards/spades/image_part_012.jpg'))
        else:
            await ctx.author.send(file=discord.File('cards/spades/image_part_013.jpg'))
    elif z == 4:
        x = rand.randint(1,13)
        if x == 1:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_001.jpg'))
        elif x == 2:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_002.jpg'))
        elif x == 3:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_003.jpg'))
        elif x == 4:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_004.jpg'))
        elif x == 5:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_005.jpg'))
        elif x == 6:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_006.jpg'))
        elif x == 7:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_007.jpg'))
        elif x == 8:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_008.jpg'))
        elif x == 9:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_009.jpg'))
        elif x == 10:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_010.jpg'))
        elif x == 11:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_011.jpg'))
        elif x == 12:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_012.jpg'))
        else:
            await ctx.author.send(file=discord.File('cards/hearts/image_part_013.jpg'))
    else:
        await ctx.send("Если что это баг")    
    #await ctx.author.send(file=discord.File('images/pika.jpg'))
    #await ctx.message.delete()



#random
@Bot.command()
async def random(ctx, content):
    line = ctx.message.content.split(' ')[1:]
    try:
        x = int(line[0])
        y = int(line[1])
        z = rand.randint(x,y)
        await ctx.send("Random number is : " + str(z))
    except Exception as e:
        raise
    await ctx.message.delete()


#ricardopack
@Bot.command()
async def r(ctx, content):
    line = ctx.message.content.split(' ')[1:]
    a = line[0]
    if a == "help":
        await ctx.send(file=discord.File('images/ricardo/help.png'))
    elif a == "ACCH":
        await ctx.send(file=discord.File('images/ricardo/ACCH.JPG'))
    elif a == "love":
        await ctx.send(file=discord.File('images/ricardo/love.JPG'))
    elif a == "approve":
        await ctx.send(file=discord.File('images/ricardo/approve.JPG'))
    elif a == "capture":
        await ctx.send(file=discord.File('images/ricardo/capture.JPG'))
    elif a == "come":
        await ctx.send(file=discord.File('images/ricardo/Come.JPG'))
    elif a == "confuse":
        await ctx.send(file=discord.File('images/ricardo/confuse.JPG'))
    elif a == "dance":
        await ctx.send(file=discord.File('images/ricardo/dance.JPG'))
    elif a == "delete":
        await ctx.send(file=discord.File('images/ricardo/delete.JPG'))
    elif a == "detected":
        await ctx.send(file=discord.File('images/ricardo/detected.JPG'))
    elif a == "funny":
        await ctx.send(file=discord.File('images/ricardo/funny.JPG'))
    elif a == "goodnight":
        await ctx.send(file=discord.File('images/ricardo/goodnight.JPG'))
    elif a == "helpme":
        await ctx.send(file=discord.File('images/ricardo/helpme.JPG'))
    elif a == "how":
        await ctx.send(file=discord.File('images/ricardo/how.JPG'))
    elif a == "iamhere":
        await ctx.send(file=discord.File('images/ricardo/iamhere.JPG'))
    elif a == "old":
        await ctx.send(file=discord.File('images/ricardo/old.JPG'))
    elif a == "olds":
        await ctx.send(file=discord.File('images/ricardo/olds.JPG'))
    elif a == "power":
        await ctx.send(file=discord.File('images/ricardo/power.JPG'))
    elif a == "prettyboy":
        await ctx.send(file=discord.File('images/ricardo/prettyboy.JPG'))
    elif a == "repeat":
        await ctx.send(file=discord.File('images/ricardo/repeat.JPG'))
    elif a == "sadly":
        await ctx.send(file=discord.File('images/ricardo/Sadly.JPG'))
    elif a == "seven":
        await ctx.send(file=discord.File('images/ricardo/seven.JPG'))
    elif a == "zaebis":
        await ctx.send(file=discord.File('images/ricardo/zaebis.JPG'))    
    elif a == "random":
        z = rand.randint(1,23)
        if z == 1:
            await ctx.send(file=discord.File('images/ricardo/help.png'))
        elif z == 2:
            await ctx.send(file=discord.File('images/ricardo/ACCH.JPG'))
        elif z == 3:
            await ctx.send(file=discord.File('images/ricardo/love.JPG'))
        elif z == 4:
            await ctx.send(file=discord.File('images/ricardo/approve.JPG'))
        elif z == 5:
            await ctx.send(file=discord.File('images/ricardo/capture.JPG'))
        elif z == 6:
            await ctx.send(file=discord.File('images/ricardo/Come.JPG'))
        elif z == 7:
            await ctx.send(file=discord.File('images/ricardo/confuse.JPG'))
        elif z == 8:
            await ctx.send(file=discord.File('images/ricardo/dance.JPG'))
        elif z == 9:
            await ctx.send(file=discord.File('images/ricardo/delete.JPG'))
        elif z == 10:
            await ctx.send(file=discord.File('images/ricardo/detected.JPG'))
        elif z == 11:
            await ctx.send(file=discord.File('images/ricardo/funny.JPG'))
        elif z == 12:
            await ctx.send(file=discord.File('images/ricardo/goodnight.JPG'))
        elif z == 13:
            await ctx.send(file=discord.File('images/ricardo/helpme.JPG'))
        elif z == 14:
            await ctx.send(file=discord.File('images/ricardo/how.JPG'))
        elif z == 15:
            await ctx.send(file=discord.File('images/ricardo/iamhere.JPG'))
        elif z == 16:
            await ctx.send(file=discord.File('images/ricardo/old.JPG'))
        elif z == 17:
            await ctx.send(file=discord.File('images/ricardo/olds.JPG'))
        elif z == 18:
            await ctx.send(file=discord.File('images/ricardo/power.JPG'))
        elif z == 19:
            await ctx.send(file=discord.File('images/ricardo/prettyboy.JPG'))
        elif z == 20:
            await ctx.send(file=discord.File('images/ricardo/repeat.JPG'))
        elif z == 21:
            await ctx.send(file=discord.File('images/ricardo/Sadly.JPG'))
        elif z == 22:
            await ctx.send(file=discord.File('images/ricardo/seven.JPG'))
        elif z == 23:
            await ctx.send(file=discord.File('images/ricardo/zaebis.JPG'))
        else:
            await ctx.send("Если что это баг")
    else:
        await ctx.send("Ты шо дурак чтоли")
    await ctx.message.delete()


@Bot.command()
async def weather(ctx):
    observation = owm.weather_at_place("Riga,LV")
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    await ctx.send("В Риге сейчас " + w.get_detailed_status())
    degree_sign = u'\N{DEGREE SIGN}'
    await ctx.send("Температра сейчас в районе " + str(temp) + degree_sign + "c")


token = ('NTk0NTc3MDkwODgwMzQwMDkz.XbsM0A.SLqjffwsDX965-de2J4xJpXbStI')



Bot.run(str(token))
