import discord
import os
from dotenv import load_dotenv
import service

client = discord.Client()
load_dotenv(os.path.join(os.getcwd(), '.env'))
SECRET_KEY = os.getenv("TOKEN")

last_user = ""
count_attempt = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def count_attempts(user):
    global last_user, count_attempt
    if last_user == user:
        count_attempt += 1
    else:
        last_user = user
        count_attempt = 0

def get_message_about_attempt():
    global count_attempt
    if count_attempt == 1:
        return "Você só tem mais uma chance hein!"
    
    if count_attempt == 2:
        return "Bora escolher! Acabaram suas chances!"
    
    return ""

def should_not_response():
    global count_attempt
    if count_attempt == 2:
        return True
    
    return False

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if should_not_response():
        await message.channel.send("Ops, suas chances acabaram. Hora de escolher!")
        return

    count_attempts(client.user)
    about_attempts = get_message_about_attempt()

    if message.content.startswith('/food'):
        suggest = service.get_food()
        await message.channel.send(suggest + "\n" + about_attempts)

    if message.content.startswith('/drink'):
        suggest = service.get_drink()
        await message.channel.send(suggest + "\n" + about_attempts)

client.run(SECRET_KEY)