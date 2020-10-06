# Name: Ahsan Khan
# Date: 10/06/20
# Description: Make a list called sandwich_orders and fill it with the names of various sandwiches.
#			   Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each other,
#              such as I make your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a 
#			   message listing each sandwich that was made.

sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'fish sandwich', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
		current_order = sandwich_orders.pop()
		if current_order == 'pastrami':
			print("We have ran out of pastramin\n")
		else:
			print(f"Making your {current_order.title()}")
			finished_sandwiches.append(current_order)

print()

for orders in finished_sandwiches:
	print(f"Your {orders} is ready.")