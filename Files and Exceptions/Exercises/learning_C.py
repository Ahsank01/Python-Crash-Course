# Name: Ahsan Khan
# Date: 10/29/20
# Description: Use replace() method to replace the words in the file.

file_name = 'learning_python.txt'

with open(file_name) as file_content:
	read_content = file_content.read()

read_content = read_content.replace('how', 'ccc')
read_content = read_content.replace('Python', 'C')
print(read_content)