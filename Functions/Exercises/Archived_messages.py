# Name: Ahsan Khan
# Date: 10/12/20
# Description: Start with the program Sending_messages.py. Call the function send_messages() with a copy of the list of messages.
#			   After calling the function, print both of yours lists to show that th original list has retained its messages


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

send_messages(messages[:], newList)
print()

print(messages)
print(newList)