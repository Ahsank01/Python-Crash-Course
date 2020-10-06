# Name: Ahsan Khan
# Date: 10/06/20
# Description: Write a program that asks the user how many people are in the dinner group. If the answer is more than eight, print
#			   a message saying they will have to wait for a table. Otherwise, report that the table is ready.

prompt = input("How many people are in the dinner group: ")
prompt = int(prompt)

if prompt > 8:
	print("\nYou will have to wait for a table.")
else:
	print("\nYour table is ready!")