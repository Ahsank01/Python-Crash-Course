# Name: Ahsan Khan
# Date: 10/12/20
# Description: Start with a copy of messages.py. Write a function called send_messages() that prints each text message and moves each message
#			   to a new list called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages
#			   were moved correctly.

def show_messages(messages):
	for message in messages:
		print(f"{message}")

def send_messages(messages, newList):
	while messages:
		currentMessage = messages.pop()
		print(f"Sending message, {currentMessage}")
		newList.append(currentMessage)

messages = ['Hi', 'How are you?', 'What do you do?']
newList = []

show_messages(messages)
print()

send_messages(messages, newList)
print()

print(messages)
print(newList)