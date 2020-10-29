# Name: Ahsan Khan
# Date: 10/13/20
# Description: Add an attribute called login_attempts to the class User. Write a method called increment_login_attempts() 
#			   that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login login_attempts to 0.

class User:
	def __init__(self, first_name, last_name, age, date_of_birth, user_name):
		self.fName = first_name
		self.lName = last_name
		self.age = age
		self.dob = date_of_birth
		self.user = user_name
		self.login_attempts = 0

	def describe_user(self):
		print(f"First Name: {self.fName.title()}")
		print(f"Last Name: {self.lName.title()}")
		print(f"Age: {self.age}")
		print(f"Date of Birth: {self.dob}")
		print(f"User Name: {self.user}")

	def greet_user(self):
		print(f"Hello, {self.user}! We are excited to have you here.")

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
		return self.login_attempts

	def show_attempts(self):
		return self.login_attempts

	def reset_login_attempts(self):
		self.login_attempts = 0


new_user1 = User('ahsan', 'khan', '20', '01/20/2000', 'ahsank20')
new_user1.describe_user()
print()

new_user1.increment_login_attempts()
new_user1.increment_login_attempts()
new_user1.increment_login_attempts()
new_user1.increment_login_attempts()
print(new_user1.show_attempts())

new_user1.reset_login_attempts()
print(new_user1.show_attempts())