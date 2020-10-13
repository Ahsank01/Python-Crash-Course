# Name: Ahsan Khan
# Date: 10/12/20
# Description: Write a function that stores information about a car in a dictionary.
#			   The function should always receive a manufacturer and a model name.
#			   It should then accept an arbitary number of keywod arguments. Call the function
#			   with the required information and two other name-value pairs, such as color or an optionak feauture.
#			   Your function should work for a call like this: car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 			   Print the dictionary that's returned to make sure all the information was stored correctly.

def car(manufacturer, model, **kwargs):
	kwargs['manufacturer'] = manufacturer
	kwargs['model'] = model 
	return kwargs

my_car = car('nissan', 'pathfinder', color='red', mode='suv')
print(my_car)
