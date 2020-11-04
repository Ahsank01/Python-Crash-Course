# Name: Ahsan Khan
# Date: 11/02/20
# Description: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file.
#			   Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch
#			   the FileNotFound error, and print a friendlt message if a file is missing.

def readFiles(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		print("The file you asked for, is not found.")
	else:
		print(contents)


filename = ['cats.txt', 'dogs.txt', 'elephant.txt']
for files in filename:
	readFiles(files)
	print()

# readFiles('cats.txt')
# readFiles('dogs.txt')