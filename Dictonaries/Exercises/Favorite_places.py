# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make a dict.. called favorited_places. Think of three names to use as keys in the dict.. and store one to three favorite places for each person.

favorited_places = {
	'ahsan':['greece', 'morocco', 'afghanistan'],
	'ayesha':['england', 'canada', 'uae'],
	'mohamed':['syria', 'israel', 'brazil'],
}

for name, place in favorited_places.items():
	print(f"\nName: {name.title()}")
	print(f"Places {name.title()} likes to visit are:")
	for places in place:
		print(f"\t{places.title()}")