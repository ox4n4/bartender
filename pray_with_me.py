import requests
import json
from pprint import pprint

# get yes ingredients
yes_input = input('What ingredient do you have? Separate each item by commas!')
str = yes_input.split(",")
avaliable = []
for i in str:
    avaliable.append(i)
print(avaliable)

# API
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearar {0}'.format(1)}
empty_list = ['']
def get_list(good):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearar {0}'.format(1)}
    url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + good
    response = requests.get(url)
    recipe = response.json()
    for count in recipe['drinks']:
        pprint(count['strDrink'])

def get_list_a(one):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearar {0}'.format(1)}
    urlone = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + one
    responseone = requests.get(urlone)
    recipeone = responseone.json()
    for count in recipeone['drinks']:
        pprint(count['strDrink'])
    return recipeone

def get_list_b(two):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearar {0}'.format(1)}
    urltwo = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + two
    responsetwo = requests.get(urltwo)
    recipetwo = responsetwo.json()
    for count in recipeone['drinks']:
        pprint(count['strDrink'])
    return recipetwo

def compare_list (three, four):
    list1_as_set = set(three)
    recipe2 = four
    intersection = list1_as_set.intersection(recipe2)
    intersection_as_list = list(intersection)
    for count in intersection['drinks']:
        pprint(count['strDrink'])
    return intersection

if int(len(avaliable)) > 1:
    for a in range(len(avaliable)):
        print(avaliable[a])
        print(avaliable[a+1])
        ana = (avaliable[a])
        oxana = (avaliable[a+1])
        c=get_list_a(ana)
        d=get_list_b(oxana)
        compare_list(c,d)
        rere_input = input('What drinks out of the list did you want to make?')
        urlre = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + rere_input
        responsere = requests.get(urlre)
        recipere = responsere.json()
        print('\n')
        for countre in recipere['drinks']:
            pprint(countre['strInstructions'])
else:
        print(avaliable[0])
        print('\n')
        print("instruction:")
        b = avaliable[0]
        get_list(b)
        re_input = input('What drinks out of the list did you want to make?')
        url2 = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + re_input
        response2 = requests.get(url2)
        recipe2 = response2.json()
        #pprint(recipe2)
        print('\n')
        for count2 in recipe2['drinks']:
            pprint(count2['strInstructions'])
