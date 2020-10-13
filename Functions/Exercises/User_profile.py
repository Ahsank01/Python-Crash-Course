# Name: Ahsan Khan
# Date: 10/12/20
# Description: Start with a user_profile.py program from the practice.  Build a profile of yourself
#			   by calling build_profile(), using your first and last name and three other ket-value pairs that describes you

def build_profile(first, last, **user_info):
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

my_info = build_profile('ahsan', 'khan', city='new york', profession='student', field='computer science')
print(my_info)