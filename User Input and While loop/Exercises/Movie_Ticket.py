# Name: Ahsan Khan
# Date: 10/06/20
# Description: MOVIE TICKET: If  person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticker is $15
#			   Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.


people = input("Enter the total number of tickets you want to purchase: ")
people = int(people)

total = 0

while people >= 1:
	t = input("Enter the age of the person: ")
	t = int(t)

	if t < 3:
		total += 0
	elif t >=3 and t <= 12:
		total += 10
	else:
		total += 15

	people -= 1

print(f"\nYour total is ${total}.")