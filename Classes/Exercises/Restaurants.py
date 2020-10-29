# Name: Ahsan Khan
# Date: 10/13/20
# Description: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: restaurant_name and cuisine_type.
#			   Make a method called describe_restaunrat() that print these two pieces of information, and a method called open_restaurant() that prints a message indicating
#			   that a the restaurant is open.


class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		print("The restaurant offers Italian, Chinese and Pakistani Cuisinse.")
		print("No dine in, due to COVID-19.")

	def open_restaurant(self):
		print("We are open, you are welcome at any time.")


# 1st Instance
my_restaurant = Restaurant('Dhabba', 'Worlwide')

print(f"We are {my_restaurant.name}")
print(f"Our {my_restaurant.name} offers {my_restaurant.cuisine} cuisine.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()

# 2nd Instance
my_restaurant2 = Restaurant('Chai Spot', 'tea')
my_restaurant2.describe_restaurant()
print()

# 3rd Instance
my_restaurant3 = Restaurant('Starbucks', 'coffee')
my_restaurant3.describe_restaurant()
print()