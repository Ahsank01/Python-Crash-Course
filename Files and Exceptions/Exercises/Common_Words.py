# Name: Ahsan Khan
# Date: 11/02/20
# Description: Write a program that would count common words from the file.

filename = 'alice.txt'

with open(filename) as f:
	contents = f.read()

contents = contents.lower()

# count the word the
wordCount = contents.count('the')
print(wordCount)

