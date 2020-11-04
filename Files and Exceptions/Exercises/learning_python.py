# Name: Ahsan Khan
# Date: 10/29/20
# Description: Read a file learning_python.txt by readying the entire file, once by looping over the file object, and once by storing the lines in a list
#			   and then working witht them outside the with block.


file_name = 'learning_python.txt'
words = ''

with open(file_name) as readFile:
	file_content = readFile.read()
print(file_content.strip())
print()

with open(file_name) as readFile:
	for content in readFile:
		print(content.strip())
print()


with open(file_name) as readFile:
	file_content = readFile.read()

for content in file_content:
	print(content)

for content in file_content:
	words += content

print(words)
print(words[:50])