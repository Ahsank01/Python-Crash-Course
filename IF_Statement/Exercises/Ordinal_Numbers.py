# Name: Ahsan Khan
# Date: 09/23/20
# Description: Print numbers 1-9 and save it to the list.

numbers = []

for num in range(1,10):
	if num == 1:
		numbers.append(f"{num}st")
	elif num == 2:
		numbers.append(f"{num}nd")
	elif num == 3:
		numbers.append(f"{num}rd")
	else:
		numbers.append(f"{num}th")

for number in numbers:
	print(number)