# Name: Ahsan Khan
# Date: 11/02/20
# Description: Write a program that prompts the user for their name. When they respond, write their name to ta file called guest.txt

guest = []

number_of_people = int(input("Enter the number of guest to invite: "))

for people in range(number_of_people):
	name = input("Name: ")
	guest.append(name)

#print(guest)

filename = 'guest.txt'

# Writing as a list
with open(filename, 'w') as file_object:
	file_object.write(str(guest) + '\n')


# Writing as a string
with open(filename, 'a') as file_object:
	for info in guest:
		file_object.write(info + '\n')