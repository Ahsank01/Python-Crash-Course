# Name: Ahsan Khan
# Date: 10/12/20
# Description: Write a function called city_country() that takes in the name of a city and its country.
#			   The function should return a string formatted like this: "Santiago, Chile"

def city_country(city, country):
	formatted = f"{city}, {country}"
	return formatted.title()

city_and_country = city_country('london', 'england')
print(city_and_country + '\n')

city_and_country = city_country('paris', 'france')
print(city_and_country + "\n")

city_and_country = city_country('istanbul', 'turkey')
print(city_and_country + "\n")