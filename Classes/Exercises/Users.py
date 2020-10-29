# Name: Ahsan Khan
# Date: 10/13/20
# Description: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes
#			   that are typically stored in a user profile.
#			   Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user()
#			   that prints a personalized gretting to the user.

class User:
	def __init__(self, first_name, last_name, age, date_of_birth, user_name):
		self.fName = first_name
		self.lName = last_name
		self.age = age
		self.dob = date_of_birth
		self.user = user_name

	def describe_user(self):
		print(f"First Name: {self.fName.title()}")
		print(f"Last Name: {self.lName.title()}")
		print(f"Age: {self.age}")
		print(f"Date of Birth: {self.dob}")
		print(f"User Name: {self.user}")

	def greet_user(self):
		print(f"Hello, {self.user}! We are excited to have you here.")


new_user1 = User('ahsan', 'khan', '20', '01/20/2000', 'ahsank20')
new_user1.describe_user()
print()
new_user1.greet_user()