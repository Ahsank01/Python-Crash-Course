# Name: Ahsan Khan
# Date: 09/21/20
# Description: Use a for loop to print multiples of 3 to 30

# First Method
#for value in range(1,31):
#	print(value*3)

# Second Method
multiples = [value*3 for value in range(1,31)]
for multiple in multiples:
	print(multiple)