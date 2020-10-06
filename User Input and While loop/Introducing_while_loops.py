# Name: Ahsan Khan
# Date: 10/06/20
# Description: Intro to while loops and user input

current_number = 1

while current_number <= 5:
	print(current_number)
	current_number += 1


# ================================================================ #

prompt = "\nTell me something, and I will repeat it back to you. "
prompt += "\nEnter 'quit' to end the program: "
message = " "

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

# ================================================================ #

# Use flag with while loop
active = True

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# ================================================================= #

# Usng break to exit the loop

while True:
	message = input(prompt)

	if message == 'quit':
		break
	else:
		print(message)

# ================================================================== #


# Using continue in a loop
current_number = 0
while current_number < 10:
	current_number +=1

	if current_number % 2 == 0:
		continue

	print(current_number)

# ================================================================== #

# Use lists with while loops

print()
unconfirmed_users = ['ahsank20', 'ak231', 'koke21']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user}.")

	confirmed_users.append(current_user)

print()

for users in confirmed_users:
	print(f"Verified User: {users}")

# ================================================================== #

# Use while loop to remove all instances of specific values from a list

my_list = ['cat','dog', 'tiger', 'cat', 'cat','elephant', 'cat']
print(my_list)

while 'cat' in my_list:
	my_list.remove('cat')

print(my_list)

# ================================================================== #

# Use dictionary with user input and while loop
responses = {}

polling_actice = True

while polling_actice:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	responses[name] = response

	repeat = input("Would you like to let another person respond? (Y/N) ")
	if repeat == 'n':
		polling_actice = False

print("\nPoll Results\n")
for name, response in responses.items():
	print(f"{name} would like to climb {response}")

print(responses)
