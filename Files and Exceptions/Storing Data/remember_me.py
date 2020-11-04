import json

# Dividing the work in 2 different functions

def get_stored_username():
	"""Get Stored Username if available"""

	filename = 'username.json'

	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Create a new name"""
	filename = 'username.json'
	username = input("Enter your name: ")
	with open(filename, 'w') as f:
		json.dump(f)


def greet_user():
	"""Greet the user"""
	username = get_stored_username()
	if username:
		comfirm = input(f"Is this the correct username, {username}? Enter Y/N: ")
		if confirm == 'Y' or 'y':
			print(f"Welcome back, {username}!")
		else:
			get_new_username()
	else:
		get_new_username()
		print(f"We will remember you next time, {username}.")

greet_user()