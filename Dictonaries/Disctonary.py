# Name: Ahsan Khan
# Date: 09/26/20
# Description: Intro to dictionary

alien_0 = {'color':'red', 'points':5}
print(alien_0['color']) 
print(alien_0['points'])

new_points = alien_0['points']
print(f"You have earned {new_points} points.")

# -------------------------------------------------------- #

# Adding more to the dictionary
alien_0 = {'color':'red', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# -------------------------------------------------------- #

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# -------------------------------------------------------- #

# Modifying values in a dictionary
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# --------------------------------------------------------- #

# Removing key-value pairs
alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

# --------------------------------------------------------- #

# A dictionary of similar objects
favorite_languages = {
	'ahsan':'python',
	'sarah':'c++',
	'edward':'ruby',
	'phil':'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print(favorite_languages['sarah'])

# -------------------------------------------------------- #

# Using get() to access values
alien_0 = {'color':'greeen', 'speed':'slow'}
# print(alien_0['points'])          --------------  Will give an error, because the key doesnt exist

point_value = alien_0.get('points', 'No value found!')
print(point_value)