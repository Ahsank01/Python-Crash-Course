# Name: Ahsan Khan
# Date: 09/29/20
# Description: Make a list of people who should take the favorite language poll.
#          	   Loop through the list of people who should take the poll.
#          	   If they have already taken the poll, print a message thanking them for responding.
#         	   If they haven't yet taken the poll, print a message inviting them to take the poll.

favorite_language = {
	'sarah':'python',
	'edward':'c++',
	'ahsan':'python',
	'john':'javascript',
}
names = ['jim', 'tom']  # empty variable to store names

for name in favorite_language.keys():
	names.append(name)

for name in sorted(names):
	if name in favorite_language.keys():
		print(f"{name.title()}, thanks for being part of the poll.")
	else:
		print(f"{name.title()}, please take the poll ASAP. Thank You!")