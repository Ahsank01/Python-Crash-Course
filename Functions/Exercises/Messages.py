# Name: Ahsan Khan
# Date: 10/12/20
# Description: Make a list of series of short text messages. Pass the list to a function called show_messages(). which prints each text message

def show_messages(messages):
	for message in messages:
		print(f"{message}")

messages = ['Hi', 'How are you?', 'What do you do?']
show_messages(messages)