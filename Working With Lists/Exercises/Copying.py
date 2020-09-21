# Name: Ahsan Khan
# Date: 09/21/20
# Description: Practice using Copying list

my_pizza = ['cheese pizza', 'chicago pizza', 'italian cheese sticks']
friends_pizza = my_pizza[:]

my_pizza.append('butter chicken pizza')
friends_pizza.append('tikka pizza')

print("Proving that both lists are different")
print(my_pizza)
print(friends_pizza)