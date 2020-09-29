# Name: Ahsan Khan
# Date: 09/29/20
# Description: Loop through a glossary in the dictionary, then print it. Then add 2 more words to the glossary and loop again.

programming_words = {
	'if':'A resevered keyword, to check the conditional statements.',
	'del':'A delete function, to delete a value from the list or dictionary, permenantly.',
	'print()':'A print function, outputs data on the screen.',
	'.strip()': 'A resevered function, being use to clear out the useless whitespace'
}

for reseveredWord, meaning in programming_words.items():
	print(f"{reseveredWord}: {meaning}")

programming_words['for'] = 'this keyword is to use a loop in the program'
programming_words['.list()'] = 'this funtion is mostly being used to the loop, to print out the items in a dictionary'
print()
print("New Dictionary")
for reseveredWord, meaning in programming_words.items():
	print(f"{reseveredWord}: {meaning}")