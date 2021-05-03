# bot.py
import os

import discord
from dotenv import load_dotenv

import requests
from io import BytesIO
#https://stackoverflow.com/a/22393884
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_GUILD = os.getenv('MY_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==MY_GUILD:
            for channel in guild.channels:
                if channel.name=="bot-usage":
                    u = requests.get("https://cdn.discordapp.com/attachments/789208552978907206/838570682102579200/videos_bruh_moment.mp4")
                    tempFile = BytesIO(u.content)
                    await channel.send(content="bruh",file=discord.File(tempFile,filename="ericisawesome.mp4"))#https://discordpy.readthedocs.io/en/stable/api.html#discord.File
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)