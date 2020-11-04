# Name: Ahsan Khan
# Date: 11/02/20
# Description: Modify the except block from Cats_and_Dogs.py to fail silently if eithrt file is missing

def readFiles(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)


filename = ['cats.txt', 'dogs.txt', 'elephant.txt']
for files in filename:
	readFiles(files)
	print()