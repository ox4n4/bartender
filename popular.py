Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> import requests
>>> api_token = '9973553'
>>> api_url_base = 'https://thecocktaildb.com/api/json'
>>> headers = { 'Content-Type': 'application/json'}
>>> headers= {'Authorization': 'Bearer {0}'.format(api_token)}
>>> def get_popular():
	api_url = '{0}v2/9973533/popular.php'.format(api_url_base)
	response = requests.get(api_url, headers=headers)
	if response.status.code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

	
>
