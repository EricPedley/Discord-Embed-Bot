# bot.py

import discord
from dotenv import load_dotenv
import re#regular expressions
import requests
from io import BytesIO
#https://stackoverflow.com/a/22393884
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
        if message.content.find("instagram.com/p"):
            webLink = re.findall(r"(www.instagram.com/p/...........)",message.content)[0]
            webResponse = requests.get(f"https://{webLink}/")
            webCode=webResponse.text
            if(webResponse.status_code>=300):
                print(f"error {webResponse.status_code}, wrote response html to file errorpage.html")
                with open("errorpage.html",'w') as f:
                    f.write(webCode)
            else:
                vidLink = re.findall(r'<meta property="og:video" content="(.+)"',webCode)[0]
                vidResponse = requests.get(vidLink)
                tempFile = BytesIO(vidResponse.content)
                await message.channel.send(file=discord.File(tempFile,filename="epic_embed_clutch.mp4"))
client.run(TOKEN)