# Name: Ahsan Khan
# Date: 10/13/20
# Description: Working with Classes

class Dog:
	""" A simple attempt to model a dog """

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in respond to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over.")



# Making an instance from a class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print()

# Maknig multiple instances
my_dog2 = Dog('Lucy', 3)\

print(f"My dog's name is {my_dog2.name}.")
print(f"My dog is {my_dog2.age} years old.")
my_dog2.sit()
my_dog2.roll_over()
print()


# ======================================================================= #

# The Car Class
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('nissan', 'pathfinder', 2005)
print(my_new_car.get_descriptive_name())

# ======================================================================= 3

# Setting a dedault value for an attribute
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car2 = Car('audi', 'a8', 2021)
print(my_new_car2.get_descriptive_name())
my_new_car2.read_odometer()
print()

# Modifying attributes value

# Modifyig it directly
my_new_car2.odometer_reading = 1000
my_new_car2.read_odometer()
print()

# =================================== #

# Modifying an attribute's valye through a method
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back on odometer reading!!!")

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car3 = Car('mercedez-benz', 'c class', 2021)
my_new_car3.update_odometer(500)
print(my_new_car3.get_descriptive_name())
my_new_car3.read_odometer()
print()
my_new_car3.update_odometer(100) # Try to rtoll back the odometer
print()

# ==================================== #

# increment odometer
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back on odometer reading!!!")

	def increment_odometer(self, addMiles):
		self.odometer_reading += addMiles

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car3 = Car('mercedez-benz', 'c class', 2021)
print(my_new_car3.get_descriptive_name())

my_new_car3.update_odometer(10000)
my_new_car3.read_odometer()

my_new_car3.increment_odometer(100)
my_new_car3.read_odometer()