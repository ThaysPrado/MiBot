import discord
import os
from dotenv import load_dotenv
import requests
import json

client = discord.Client()
load_dotenv(os.path.join(os.getcwd(), '.env'))
SECRET_KEY = os.getenv("TOKEN")

def get_suggest():
    response = requests.get("https://themealdb.com/api/json/v1/1/random.php")
    json_data = json.loads(response.text)
    meal = json_data["meals"][0]
    area = meal["strArea"]
    mealSuggest = meal["strMeal"]
    source = meal["strSource"]
    response = "Sugestão do MiBot:\n" + area + "\nPrato: " + mealSuggest + "\nReceita: " + source
    return(response)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        suggest = get_suggest()
        await message.channel.send(suggest)

client.run(SECRET_KEY)