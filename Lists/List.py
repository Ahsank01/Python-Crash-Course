# Name: Ahsan Khan
# Date: 09/16/20
# Description: Introduction to list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2])

# -------------------------------------------------------------- # 

# Python has a special syntax for accessing the last element in a list. 
# By asking for the item at index -1, Python always returns the last item in the list:
# Index -2 will return the second last item from the list. -3 returns third item from the last, and so on.....
print(bicycles[-1])
print(bicycles[-3])

# -------------------------------------------------------------- #

# Use f-string with lists
print(f"My first bicycle was a {bicycles[1].title()}.")

# -------------------------------------------------------------- #

# Modifying elements in the list:

# CHANGING an element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'		# Changing the element on index[0]
print(motorcycles)

# ADDING an element
motorcycles.append('honda')
print(motorcycles)

# Starting with an empty list.
new_motorcycle_list = []
new_motorcycle_list.append('honda')
new_motorcycle_list.append('kawasaki')
new_motorcycle_list.append('ducati')
print(new_motorcycle_list)

# Inserting an element in the list
new_motorcycle_list.insert(1, 'yamaha')
print(new_motorcycle_list)

# Removing an item from the list
# If you know the position of the item you want to remove from a list,
# you can use the del statement.
print(new_motorcycle_list)
del new_motorcycle_list[1]
print(new_motorcycle_list)
del new_motorcycle_list[0]
print(new_motorcycle_list)

# Removing an item using the pop() method
motorcycle_list = ['honda', 'yamaha', 'kawasaki', 'ducati', 'suzuki']
popped_list = motorcycle_list.pop()
print(motorcycle_list)
print(popped_list)

last_owned = popped_list
print(f"The last motorcycle I owned was, {last_owned.upper()}.")

# Popping items from any position in a list
first_owned = motorcycle_list.pop(0)
print(f"The first motorcycle I owned was a, {first_owned.title()}.")

# Removing an item by VALUE
motorcycle_list = ['honda', 'yamaha', 'kawasaki', 'ducati', 'suzuki']
print(motorcycle_list)
motorcycle_list.remove('kawasaki')
print(motorcycle_list)

too_expensive = 'ducati'
motorcycle_list.remove(too_expensive)
print(motorcycle_list)
print(f"A {too_expensive.title()} is way too expensive for me!")

# ------------------------------------------------------------ #

# Sorting the list

# sort function
cars = ['honda', 'bmw', 'cadillac', 'mercedes', 'toyota', 'chevy']
print(cars)
cars.sort()
print(cars)

# Reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# ------------------------------------------------------------- #

# Sorting a list temporarily with the sorted() function
new_cars = ['mercedes', 'honda', 'bmw', 'cadillac']
print(new_cars) # Not sorted
print(sorted(new_cars)) # Sorted
print(new_cars) # Not sorted again
new_cars.reverse()
print(new_cars)

# ------------------------------------------------------------- #

# Find the length of a list
cars = ['honda', 'bmw', 'cadillac', 'mercedes', 'toyota', 'chevy']
print(len(cars))