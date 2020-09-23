# Name: Ahsan Khan
# Date: 09/23/20
# Description: Check if the username is already taken.

current_users = ['Admin', 'AK679', 'khan312', 'linuxuser', 'nouserhere']
new_users = ['windowsuser', 'techie', 'admin', 'ak679', 'newuser']
copy_current_users = []

# making everything in lower alphabets
for current_user in current_users:
	copy_current_users.append(current_user.lower())

for new_user in new_users:
	if new_user in copy_current_users:
		print(f"{new_user}, username is not available.")
	else:
		print(f"{new_user}, is available.")
