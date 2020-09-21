# Name: Ahsan Khan
# Date: 09/16/20
# Description: This program is to practice with these 3 functions with the list: (reverse(), sorted(), sort())

# Think of at least five places in the world you'd like to visit.
places = ['Greece', 'Afghanistan', 'Turkey', 'Syria', 'Israel']

# Print the list in original order.
print(f"Original Order: {places}")

# Sorting the list without modifying the original list
print(f"Sorted Order: {sorted(places)}")

# Show the the original form of the list still exists.
print(f"Original Order: {places}")

# Use sorted() to reverse print the list
print(f"Reverse Order: {sorted(places, reverse=True)}")

# Show the the original form of the list still exists.
print(f"Original Order: {places}")

# Use reverse to change the order of the list
places.reverse()
print(f"Reversed Order: {places}")

# Use reverse to change the order of the list again\
places.reverse()
print(f"Reversed Order: {places}")

# Sort the list permenantly
places.sort()
print(f"Sorted Order: {places}")

# Sort the above list in a reverse order
places.sort(reverse=True)
print(f"Reversed Sorted Order: {places}")