# Name: Ahsan Khan
# Date: 09/21/20
# Description: Practice using SLICES

food_list = ['chocolate cake', 'pizza', 'chicken burger', 'cheese burger', 'lasagna', 'tuna sandwich']

print("The first 3 items in the list are:")
for first in food_list[:3]:
	print(first.title())

print("\nThree items from the middle of the list are:")
for middle in food_list[2:5]:
	print(middle.title())

print("\nThe last three items in the list are:")
for last in food_list[-3:]:
	print(last.title())