# Name: Ahsan Khan
# Date: 010/06/20
# Description: Become familiar with user input and while loops.


# STRING INPUT
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(name)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"\nHello, {name}!")

# ----------------------------------------------------------------------------------- #

# INTEGER INPUT
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nYou are tall enough to ride!")
else:
	print("\nYou will be able to ride when you are a bit older.")


# ==================================================================================== #

# Even or Odd
number = input("Enter a number, I wil tell you if it is even or odd: ")
number = int(number)

if number % 2==0:
	print("\nEven")
else:
	prin("\nOdd")