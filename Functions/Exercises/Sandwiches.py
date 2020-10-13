# Name: Ahsan Khan
# Date: 10/12/20
# Description: Write a function that accepts a list of items a person wants on a sandwich. 
#			   The function should have one parameter that collects as many items as the function call provides, and it should print a summary
#			   of the sandwich that's being ordered. Call the function three times, using a different number of arguments each time.

def build_sandwich(*items):
	print("Making your sandwich with the following items:")

	for item in items:
		print(f"- {item.title()}")

sandiwch = build_sandwich('chicken', 'tuna', 'fries')
print()

sandiwch = build_sandwich('fish', 'kofta')
print()

sandiwch = build_sandwich('beef pettie', 'salad')
print()