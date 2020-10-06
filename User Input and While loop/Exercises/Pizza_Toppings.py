# Name: Ahsan Khan
# Date: 10/06/20
# Description: Write a loop that prompts the user to enter a series of pizza toppings, until they enter 'quit' value.
#			   As they enter each topping, print a message saying you will add that topping to their pizza.

active = True

while active:
	prompt = input("Enter a series of pizza toppings, one at a time.\nEnter 'quit' to quit the program: ")
	if prompt == 'quit':
		active = False
	else:
		print(f"\n{prompt} has been added on your pizza.\n")