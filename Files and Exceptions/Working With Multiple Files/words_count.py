def count_words(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print("File Not Found")
	else:
		words = contents.split()
		wordLength = len(words)
		print(f"The file '{filename}', has about {wordLength} words.")
		
filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'beast_jewel.txt', 'bear_trust.txt', 'pi_digits.txt']

for files in filenames:
	count_words(files)