import requests
import json
from pprint import pprint

# #get yes ingredients
# yes_input = input('What ingredient do you have? Separate each item by commas!')
# str = yes_input.split (",")
# avaliable = []
# for i in str:
# 	avaliable.append(i)
# print (avaliable)
#
# #get the no ingredients
# no_input = input("What ingredient don't you want in the drink? Separate each item by commas!")
# str2 = no_input.split (",")
# unavaliable = []
#for i in str2:
# 	unavaliable.append(i)
# print (unavaliable)

yes_input = input('What key ingredient do want to use?')


#url = 'https://pokeapi.co/api/v2/pokemon/􏰆􏰈{}/'.format(pokemon_number)
#response = requests.get(url)
#print(response)
#pokemon = response.json()
#pprint(pokemon)


#API stuff THIS IS BS
headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearar {0}'.format(1)}
url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i='+ yes_input
response = requests.get(url)

recipe = response.json()
#pprint(recipe)
for count in recipe['drinks']:
    pprint(count['strDrink'])

re_input = input('What drinks out of the list did you want to make?')
url2 = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='+ re_input
response2 = requests.get(url2)
recipe2 = response2.json()
for count2 in recipe2['drinks']:
    pprint(count['strInstructions'])
