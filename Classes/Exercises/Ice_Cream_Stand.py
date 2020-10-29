# Name: Ahsan Khan
# Date: 10/28/20
# Description: Write a class called IceCreamStand that inherits from the Restaurant class from the previous exercise.
#			   Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays 
#			   these flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
#			   Create an instance of IceCreamStand, and cal this method.


class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		print("The restaurant offers Italian, Chinese and Pakistani Cuisinse.")
		print("No dine in, due to COVID-19.")

	def open_restaurant(self):
		print("We are open, you are welcome at any time.")



class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'strawberry', 'vanilla']


	def iceCreamFlavors(self):
		for flavor in self.flavors:
			print(flavor)


myIceCream = IceCreamStand('ice cream stand' , 'ice cream')

myIceCream.iceCreamFlavors()