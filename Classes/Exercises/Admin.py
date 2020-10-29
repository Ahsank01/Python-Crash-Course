# Name: Ahsan Khan
# Date: 10/28/20
# Description: Write a class called Admin that inherits from the User class from the previous User class. Add an attribute
#			   called, privilegesm, that stores a list of strings like "can add "post, "can delete post", "can ban user", and so on.
#			   Write a method called sjow_privileges() that lists the administrators's set of privileges. 

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
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege.title())


admin = Admin('ahsan', 'khan', 20, '01/20/2000', 'ahsank1010')
admin.show_privileges()