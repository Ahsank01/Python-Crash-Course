import json

# Name: Ahsan Khan
# Date: 11/02/20
"""Description: Write a program that prompts for the user's favorite number. Use json.dump() to store this number in a file. Write a separate prorgam
				that reads in this value and prints the message. "I know your favorite number! It's ______"! """

def get_favorite_number():
	"""Get the fav number if available"""
	filename = 'favorite_number.json'
	
	try:
		with open(filename, 'r') as f:
			favorite_number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite_number


def get_new_favorite_number():
	"""Get a favorite number, if not already stored"""
	filename = 'favorite_number.json'
	favorite_number = input("Enter your favorite number: ")
	favorite_number = int(favorite_number)

	with open(filename, 'w') as f:
		json.dump(f)

def show_favorite_number():
	favorite_number = get_favorite_number()

	if favorite_number:
		print(f"I know your favorite number, it is {favorite_number}!!")
	else:
		get_new_favorite_number()
		print("We will remember your favorite number next time you come!!")

show_favorite_number()