# Name: Ahsan Khan
# Date: 10/28/20
# Description: Write a separae Privileges class. the class should have one attribute, privileges, that stores a list 
#			   of strings as described in Admin.py class. Move the show_privileges() method to this class. Make a Privileges instance as an
#			   attribute in the Admin class. Create a new instance of Admin and sue your method to show its privileges.

class Privileges:
	def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege.title())

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


class Admin(User):
	def __init__(self, first_name, last_name, age, date_of_birth, user_name):
		super().__init__(first_name, last_name, age, date_of_birth, user_name)
		self.privileges = Privileges()


admin = Admin('ahsan', 'khan', 20, '01/20/2000', 'ahsank1010')
#admin.describe_user()
#admin.privileges.show_privileges()
admin.privileges.show_privileges()
