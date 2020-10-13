# Name: Ahsan Khan
# Date: 10/11/20
# Description: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#    	 	   The function should print a sentence summarizing the size of the shirt and the message printed on it.
#              Call the function with positional and keyword arguement.

def make_shirt(size, text):
	print(f"You ordered a {size} size t-shirt, with this text on the shirt '{text}'.\n")

make_shirt('Large', 'Ahsan Khan')
make_shirt('Small', 'Ahsan Khan')


# Modify the make_shirt() function so the size is large by default and text should be 'I love Python'.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'large', text = 'I Love Python'):
	print(f"You ordered a {size} t-shirt, with this text on the shirt '{text}'.\n")

make_shirt()
make_shirt('medium')
make_shirt('small', 'I like iOS Development')