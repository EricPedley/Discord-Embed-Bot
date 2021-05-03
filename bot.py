# bot.py
import os

import discord
from dotenv import load_dotenv

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
                    myFile = open("videos/bruh moment.mp4",'rb')
                    await channel.send(content="bruh",file=discord.File(myFile))
                    myFile.close()
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)