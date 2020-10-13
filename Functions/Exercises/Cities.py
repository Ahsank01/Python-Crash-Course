# Name: Ahsan Khan
# Date: 10/11/20
# Description: Write a function called describe_city() that accepts the name of a city and its country.
#			   The function should print a simple sentence, such as Reykjavik is in Iceland. Give the
#			   parameter for the country a default value. Call your function for three cities, at least one of which
#			   is not in the default country.

def describe_city(city = 'new york', country = 'usa'):
	if country == 'usa' or country == 'uae' or country == 'uk':
		country = country.upper()
	else:
		country = country.title()
	
	city = city.title()

	print(f"{city} is in {country}.\n")\


describe_city()
describe_city('buffalo')
describe_city('chicago')
describe_city('london', 'uk')