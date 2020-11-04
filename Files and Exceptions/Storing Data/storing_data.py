import json

numbers = [1,2,3,34,4,5,3,24,3]

filename = 'numbers.json'

with open(filename, 'w') as f:
	json.dump(numbers, f)


# ======================================================== #

# Store user input data

username = input("What is your name: ")

filename = 'username.json'

with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We will remember you when you come back, {username}.")
