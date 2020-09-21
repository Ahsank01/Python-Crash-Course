# Name: Ahsan Khan
# Date: 09/21/20
# Description: Using loops to work with lists

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your text trick, {magician}.\n")

print("Thank you everyone. That was a great magic show!")

# --------------------------------------------------------------------- #

# Making numerical lists
# Python's RANGE() function makes it easy to generate a series of number
for value in range(1,6):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

# ---------------------------------------------------------------------- #

# Simple Statistics
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

# ---------------------------------------------------------------------- #

# Comprehensive List
squares = [value**2 for value in range(1,11)]
print(squares)

# ---------------------------------------------------------------------- #

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# ---------------------------------------------------------------------- #

# Looping the slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first 3 players on my team:")
for player in players[:3]:
	print(player.title())

# ---------------------------------------------------------------------- #

# Copying a list
my_foods = ['pizza', 'falafel', 'chocolate cake']
frieds_food = my_foods[:]
my_foods.append('burgers')
frieds_food.append('fish')
print("My favorite foods are:", my_foods)
print("\nMy friend's favorite foods are:", frieds_food)

# ---------------------------------------------------------------------- #

# TUPLES
# Tuples cannot be changed, like lists
dimensions = (200, 50)
print(dimensions[0], dimensions[1])
# dimensions[0] = 250 ---- CANNOT CHANGE A VALUE IN TUPLE

print("\nOriginal Dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 200)
print("\nModifed Dimensions:89`")
for dimension in dimensions:
	print(dimension)