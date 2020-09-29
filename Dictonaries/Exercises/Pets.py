# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make several dict.. where each dict.. represents a different pet. Include the kind of animal and the owner's name. Store it in list, and loop it.

pets = {'cat':['ahsan'], 'dog':['tom'], 'parrot':['mohamed']}

for pet, owner in pets.items():
	print(f"Pet: {pet.title()}")
	for name in owner:
		print(f"Owner: {name.title()}\n")