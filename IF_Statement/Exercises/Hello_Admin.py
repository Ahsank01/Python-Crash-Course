# Name: Ahsan Khan
# Date: 09/23/20
# Description: Make a list of 5 usernames, including the name 'admin'. Print greeting to each user and a special greeting for the user 'admin'.


usernames = ['admin', 'ak679', 'khan312', 'linuxuser', 'nouserhere']
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username}, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for logging in again.")
else:
	print("No username found!")

print()

# Testing with an empty list
usernames =[]
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username}, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for logging in again.")
else:
	print("No username found!")