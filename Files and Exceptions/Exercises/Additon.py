# Name: Ahsan Khan
# Date: 11/02/20
# Description: One common problem when prompting for numerical inpuy occurs when people provide text instead of numbers. When you try to convert the input to an int,
#			   you will get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number,
#			   and print a friendly error message. Test your program by entering two numbers and then entering some text instead of a number.

print("Enter two numbers and I will give you the sum of it!")
print("Enter 'q' at anytime to quit!!\n")


while True:
	no1 = input("Number 1: ")
	if no1 == 'q':
		break

	no2 = input("Number 2: ")
	if no2 == 'q':
		break
	try:
		no1 = int(no1)
		no2 = int(no2)
		sum = no1 + no2
	except ValueError:
		print("You did not enter a digit!")
	else:
		print(sum)