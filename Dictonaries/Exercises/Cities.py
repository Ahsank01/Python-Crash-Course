# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make a dict.. called cities. Use the names of three cities as keys in your dict.
#			   Creat a dict.. of information about each city and include the country that the city is in, population, one fact.

cities = {
	'new york': {
		'country':'usa',
		'population':'8.8M',
		'fun_fact':'tall buildings',
	},
	'san francisco': {
		'country':'usa',
		'population':'5.5M',
		'fun_fact':'tech hub',
	},
	'dubai':{
		'country':'uae',
		'population':'3M',
		'fun_fact':'7 star hotel'
	}
}

for city, city_info in cities.items():
	print(f"City: {city.title()}")
	print(f"\tCountry: {city_info['country'].upper()}")
	print(f"\tPopulation: {city_info['population']}")
	print(F"\tFun Fact: {city_info['fun_fact']}\n")