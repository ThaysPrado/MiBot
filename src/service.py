import requests
import json

mealAPI = "https://themealdb.com/api/json/v1/1/random.php"
drinkAPI = "https://thecocktaildb.com/api/json/v1/1/random.php"

def get_food():
    response = requests.get(mealAPI)
    json_data = json.loads(response.text)
    meal = json_data["meals"][0]
    area = meal["strArea"]
    mealSuggest = meal["strMeal"]
    source = meal["strSource"]
    text = "**Sugestão do MiBot**:\nTipo: " + area + "\nPrato: " + mealSuggest + "\nReceita: " + source
    return(text)

def get_drink():
    response = requests.get(drinkAPI)
    json_data = json.loads(response.text)
    drink = json_data["drinks"][0]["strDrink"]
    text = "**Sugestão do MiBot**:\n" + drink
    return(text)

def get_introduction():
    text = '''Oie, sou a **MiBot!**
Com o comando ``/food`` você pode sortear uma sugestão de comida.
Com o comando ``/drink`` você pode sortear uma sugestão de bebida.
Cuidado, para não termos problemas com as apis usadas, optei por limitar a quantidade de tentativas por usuário.
    '''
    return(text)