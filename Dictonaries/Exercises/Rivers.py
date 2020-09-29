# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make a dictionary containing three major rivers and the country.
#              Use a loop to print a sentence
#              Use a loop to print the name of the rivers
#              Use a loop to print the name of the country

rivers = {
	'nile':'egypt',
	'mississippi':'usa',
	'amazon river':'brazil',
}

for river, country in rivers.items():
	if country == 'usa':
		print(f"{river.title()} runs through {country.upper()}.")
	else:
		print(f"{river.title()} runs through {country.title()}")
print()

print("Name of the rivers:")
for river in sorted(rivers.keys()):
	print(river.title())
print()

print("Name of the countries:")
for country in sorted(rivers.values()):
	if country == 'usa':
		print(country.upper())
	else:
		print(country.title())