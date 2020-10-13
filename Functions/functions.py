# Name: Ahsan Khan
# Date: 10/07/20
# Description: Work with functions

def greet_user():
	print("Hello!")

greet_user()

# ============================================================== #

# Passing Parameters
def greet_user(username):
	print("\nHello " + username)

greet_user('Ahsan')

# ============================================================== #

# Positional Arguments
def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.\n")

describe_pet('cat', 'Mish-she')

# Calling a function multiple times
describe_pet('dog', 'Willie')

# ============================================================== #

# Keyword Argument
def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.\n")

describe_pet(animal_type = 'hamstwer', pet_name = 'Harry')

# ============================================================== #

# Default Values
def describe_pet(pet_name, animal_type = 'dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.\n")

describe_pet('harry')

# ============================================================== #

# Return Values
def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician + "\n")

# ============================================================== #

# Making an Arugement Optional
def get_formatted_name(first_name, middle_name, last_name):
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('ahsan', 'ahmed', 'khan')
print(musician + "\n")

# Make middle name Optional
def get_formatted_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name.title()

musician = get_formatted_name('ahsan', 'khan', 'ahmed')
print(musician + "\n")

musician = get_formatted_name('ahsan', 'khan')
print(musician + "\n")

# ============================================================ #

# Returning a dictionary
def build_person(first_name, last_name):
	person = {'first':first_name, 'last':last_name}
	return person

musician = build_person('ahsan', 'khan')
print(f"{musician} \n")

def build_person(first_name, last_name, age=None):
	person = {'first':first_name, 'last':last_name, 'age':age}
	return person

musician = build_person('ahsan', 'khan', 20)
print(f"{musician}\n")

# ========================================================== #

# Usng a function with a while loop
'''
def get_formatted_name(first_name, last_name):
	name = f"{first_name} {last_name}"
	return name

while True:
	print("Please tell me your name:")
	print("Enter 'q' at any time to quit!")

	f_name = input("First Name: ")
	if f_name == 'q':
		break

	l_name = input("Last Name: ")
	if l_name == 'q':
		break
	
	formatted_name = f"{f_name} {l_name}"
	print(formatted_name.title() + "\n")
'''

# ======================================================== #

# Passing a list
def greet_user(names):
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

username = ['ahsan', 'ahmed', 'khan']
greet_user(username)
print()

# ======================================================== #

# Making a list of a function

# Without a function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# Display
print("\nThe following models have been printed")
for completed in completed_models:
	print(completed.title())
print()

# With FUNCTIONS 
def printing_design(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design.title()}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed")
	for model in completed_models:
		print(model.title())

unprinted_designs = ['phone case', 'laptop case', 'airpods case']
completed_models = []

#printing_design(unprinted_designs[:], completed_models) # To send a copy of unprinted_designs
printing_design(unprinted_designs, completed_models) # To permenantly delete the data from unprinted_designs
show_completed_models(completed_models)
print(unprinted_designs[:])
print()

# ===================================================== #

# Passing an Arbitary Number of Arguments
def make_pizza(*toppings):
	print(toppings)

make_pizza('cheese')
make_pizza('chicken', 'pepperoni', 'olives')

def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
make_pizza('chicken', 'extra cheese', 'mushrooms')
print()

# ====================================================== #

# Mixibg Positinals and Arbitary Arguements
def make_pizza(size, *toppings):
	print(f"Making a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(20, 'onions', 'chicken', 'pepperoni')
print()

# ====================================================== #

# Using Arbitary Keyword Arguements

def build_portfolio(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_portfolio('ahsan', 'khan', location='new york', field='computer science')
print(user_profile)