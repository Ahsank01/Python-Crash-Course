# Name: Ahsan Khan
# Date: 10/06/20
# Description: write a program that polls users about their dream vacation. Write a promt similar to 'if you could visit one place in the world', where would you g?
#			   Print a result of the poll


active = True

dic = {}

while active:
	name = input("Can I know your name please? ")
	question = input(f"{name}, if you could visit one place in the world, where would you go? ")

	dic[name] = question

	confirm = input("Would you like to go for another reponse? (Y/N) ")
	if confirm == 'n':
		break
	else: 
		continue

for name, place in dic.items():
	print(f"{name.title()} would like to go to {place.title()} for vacations.")