# Name: Ahsan Khan
# Date: 09/21/20
# Description: Practice using TUPLES

# A buffet-style restaurant offers only five basic foods.
buffet = ('chicken curry', 'fried rice', 'noodles', 'dumplings', 'butter chicken')
print("Old Buffet:")
for food in buffet:
	print(food.title())

# Try to modify the tuple
# buffet[3] = ('etc')     ----------- CANNOT MODIFY THE TUPLE

# Change the tuple
buffet = ('chicken curry', 'fried rice', 'noodles', 'fish', 'plain rice')
print("\nNew Buffet:")
for food in buffet:
	print(food.title())