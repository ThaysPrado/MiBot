import discord
import os
from dotenv import load_dotenv
import service

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
load_dotenv(os.path.join(os.getcwd(), '.env'))
SECRET_KEY = os.getenv("TOKEN")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send(service.get_introduction())

    if message.content.startswith('/food'):
        suggest = service.get_food()
        await message.channel.send(suggest)

    if message.content.startswith('/drink'):
        suggest = service.get_drink()
        await message.channel.send(suggest)

client.run(SECRET_KEY)