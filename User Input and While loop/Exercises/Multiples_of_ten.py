# Name: Ahsan Khan
# Date: 10/06/20
# Description: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

multiple = input("Enter a number to see if it is a multiple of 10: ")
multiple = int(multiple)

if multiple % 10 == 0:
	print(f"\n{multiple}, is a multiple of 10")
else:
	print(f"\n{multiple}, is not a multiple of 10")