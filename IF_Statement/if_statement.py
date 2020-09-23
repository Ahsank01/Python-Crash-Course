# Name: Ahsan Khan
# Date: 09/23/20
# Description: Get familiar with Python IF STATEMENT

cars = ['honda', 'mercedes', 'toyota', 'bmw']

for car in cars:
	if car == 'bmw':
		print(car.upper())   
	else:
		print(car.title())

# --------------------------------------------------------- #

#Checking for inequality
requested_topping = 'mushrooms'
print( )
if requested_topping != 'anchovies':
	print("Hold the anchovies")

answer = 17
if answer != 42:
	print("\nThat is not the correct answer! Please try again.")

# --------------------------------------------------------- #

#Using AND to check multiple conditions
age_0 = 22
age_1 = 18
answer = True

if age_0 >=21 and age_1 >= 21:
	print(answer)
else:
	answer = False
	print(answer)
print()

# --------------------------------------------------------- #

# Using OR to check multiple conditions
age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:
	print(True)
else:
	print(False)
print()

# ---------------------------------------------------------- #

# Checking weather a value is in a list
requested_toppings = ['mushrooms', 'onions', 'chicken']

if 'olives' in requested_toppings:
	print(True)
else:
	print(False)
print()

# ---------------------------------------------------------- #

# Checking weather a value is not in the list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you may post a comment.")
else:
	print("You are banned!")
print()

# ---------------------------------------------------------- #

# Simple if-else statement
age = 17

if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Come back in", 18-age, "year(s). ")
print()

# ---------------------------------------------------------- #

# if-elif-else

#amusement park entry cost
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age <= 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cose is $40.")
print()

# Using multiple elif blocks
age = 35
price = 0

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")