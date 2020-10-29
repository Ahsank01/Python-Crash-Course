# Name: Ahsan Khan
# Date: 10/13/20
# Description: Start with the program Restaurants.py
"""
			   Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class.
			   Print the number of customers the restaurtant has served, and then change this value and print it again.
			   Add a method called set_number_served() that lets you set the number of customers that have been served.
			   Call this method with a new number and print the value again.
"""

class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
		self.served = 0

	def describe_restaurant(self):
		print("The restaurant offers Italian, Chinese and Pakistani Cuisinse.")
		print("No dine in, due to COVID-19.")

	def open_restaurant(self):
		print("We are open, you are welcome at any time.")

	def set_number_served(self, people_served):
		self.served += people_served


restaurant = Restaurant('Chai Spot', 'tea')
print(f"Number of people we have served: {restaurant.served}\n")

restaurant.served = 10
print(f"Number of people we have served: {restaurant.served}\n")

restaurant.set_number_served(20)
print(f"Number of people we have served: {restaurant.served}\n")