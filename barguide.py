import requests

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

