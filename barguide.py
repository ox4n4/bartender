import requests
import json

headers = { 'Content-Type': 'application/json'}

def get_cocktail():
    api_url_base = 'https://www.thecocktaildb.com/api/json/v2/9973553/popular.php'
    api_token = '9973553'

    response = requests.get(api_url, headers=headers)

    if response.status.code == 200:
            return json.loads(response.cotent.decode('utf-8'))
        else:
            return None

cocktail_info = get_recipe()

if cocktail_info is not None:
    print("Found the recipe for popular drink")
    for cocktail in cocktail_info.items():
        print(cocktail)

else:
    print('Request failure')

def cocktail_search(ingridient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid=552"
    app_key = "1"
    results = requests.get()
    ""
    data=result.json()

    return data['hits']

def run():
    ingridient=input('Enter an ingridient:')

    results=recipe_search(ingridient)

    for results in results:
        recipe=result['recipe']

        print(recipe['label'])
        print(recipe['uri'])
        print()


run()

