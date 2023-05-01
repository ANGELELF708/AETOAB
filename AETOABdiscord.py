import time 
time.clock = time.time
import discord
from discord.ext import commands
import AETOABsource
from AETOABsource import respond, setup
import pyttsx3
import engineio
from discord import FFmpegPCMAudio # Import FFmpegPCAudio from the discord library
import requests # Import the requests library
import json # Import the json library
import ffmpeg

#--SPEECH RECOGNITION--
#with open('speechResults.json', 'r') as f:
  #speechResults = json.load(f)

#--AETOAB STUFF--
setup()
#--DISCORD STUFF--
discordToken = "MTEwMDIyODU0ODUyODE3NzI4Mg.GN-acC.309bR5C7bKIqlziyhPd1ZUx6hvpoTOmh6Cfegg"
discordChannelID = 1098455638289428550

bot = commands.Bot(command_prefix="ae!", intents=discord.Intents.all())

#--TTS STUFF

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('voice', voices[0].id)
engineio.setProperty('rate', 150)

def TTSave(TTString):
    engineio.save_to_file(TTString, 'TTString.mp3')
    engineio.runAndWait()

contentFilter = ["nigger", "nigga", "fuck", "shit", "bitch", "motherfucker", "ass", "asshole", "dick", "pussy", "faggot", "fag", "nazi", "nager", "osama", "laden", "hitler", "twin towers", "osama bin laden", "fa.g", "monkey", "meth", "naeger", "neger"]

@bot.command()
async def s(ctx, *, arg):
    print(arg)
    response = respond(arg)
    for word in contentFilter:
        response = response.lower()
        response = response.replace(word, "*")
    print(response)
    await ctx.send(str(response))
    if(isConnected):
        TTSave(response)
        voice = ctx.voice_client
        #voice = await channel.connect()
        source = FFmpegPCMAudio("TTString.mp3")
        player = voice.play(source)

@bot.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("TTString.mp3")
        player = voice.play(source)
        #pass    
    else:
        ctx.send("Join a VC first dumbass!")

@bot.command()
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye everyone!")
    else: 
        await ctx.send("I'm not even in VC. Shut up loser!")

def isConnected(ctx):
    voice_client = ctx.bot.voice_clients
    return voice_client and voice_client.is_connected()

bot.run(discordToken)
