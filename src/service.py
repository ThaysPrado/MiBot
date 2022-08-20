import requests
import json

mealAPI = "https://themealdb.com/api/json/v1/1/random.php"
drinkAPI = "https://thecocktaildb.com/api/json/v1/1/random.php"

def get_food():
    response = requests.get(mealAPI)
    json_data = json.loads(response.text)
    meal = json_data["meals"][0]

    text = "**Sugestão do MiBot**:"
    if meal["strArea"] is not None:
        text += "\nTipo: "+ meal["strArea"]
    if meal["strMeal"] is not None:
        text += "\nPrato: " + meal["strMeal"]
    if meal["strSource"] is not None:
        text += "\nReceita: " + meal["strSource"]
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
    '''
    return(text)