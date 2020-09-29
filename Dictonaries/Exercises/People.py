# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make dictionaries representing different people, and store all three dictionaries in a list called people.
#              Loop through a list of people. As you loop through the list, print everything you know about each person.

people = {
	'ahsan': {
		'first_name':'ahsan',
		'last_name':'khan',
		'age':20,
		'location':'new york',
	},
	'mohamed': {
		'first_name':'mohamed',
		'last_name':'jerry',
		'age':45,
		'location':'istanbul',
	},
	'sarah': {
		'first_name':'sarah',
		'last_name':'cruise',
		'age':18,
		'location':'london',
	},
}

for person, person_info in people.items():
	print(f"Person: {person.upper()}")
	full_name = (f"{person_info['first_name'].title()} {person_info['last_name'].title()}")
	age = person_info['age']
	location = (person_info['location'].title())

	print(f"\tFull Name: {full_name}")
	print(f"\tAge: {age}")
	print(f"\tLocation: {location}\n")