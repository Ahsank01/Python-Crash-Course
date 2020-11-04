import json

filename = 'numbers.json'

with open(filename, 'r') as f:
	numbers = json.load(f)

print(numbers)

# ======================================== #

# Greet user
filename = 'username.json'

with open(filename, 'r') as f:
	username = json.load(f)
	print(f"Welcome, {username}!")