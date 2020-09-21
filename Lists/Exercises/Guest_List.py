# Name: Ahsan Khan
# Date: 09/16/20
# Description: The goal of this program is play with list and the different built-in list functions.

# GUEST LIST: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a lost that includes at least three people you'd like to invite to dinner. Then use your
# list to print a message to each person, inviting them to dinner.
guest_list = ['friend', 'professor', 'boss']

print("1st PROGGRAM")
print(f"Hello, {guest_list[0].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Good Afternoon, {guest_list[0].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Hey, {guest_list[0].title()}! I would like to invite you for a dinner at my place, tonight.")
print("END")

# CHANGING GUEST LIST: You just heard that one of your guests can't make it to the dinner, so you need to send out a new set of invitations.
# You'll have to think of someone else to invite.
print("\n2nd PROGRAM")
print(f"{guest_list[-1].title()} won't be able to make it to the dinner, tonight!\n")

guest_list[-1] = 'teacher' # Replacing boss with teacher, in the list.
print(f"Hello, {guest_list[0].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Good Afternoon, {guest_list[1].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Hey, {guest_list[2].title()}! I would like to invite you for a dinner at my place, tonight.")
print("END\n")

# ADDING MORE GUESTS: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner and send a new invite to everyone again!
print("3rd PROGRAM")
print(f"Attention {guest_list[0]}, {guest_list[1]} and {guest_list[2]}. I have found a bigger dinner table, so I will be inviting 3 more people to the dinner, tonight.\n")

guest_list.insert(0, 'Sister')
guest_list.insert(2, 'brother')
guest_list.append('coach')
print(f"Hello, {guest_list[0].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Hey, {guest_list[1].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Wassup, {guest_list[2].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Good Afternoon, {guest_list[3].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Hello, {guest_list[4].title()}! I would like to invite you for a dinner at my place, tonight.")
print(f"Hey, {guest_list[5].title()}! I would like to invite you for a dinner at my place, tonight.")
print("END\n")

# SHRINKING GUEST LIST: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
print("4th PROGRAM")
print("Due to the late arrival of my dining table, I will only be able to invite two people to the dinner.")

removed_guest = guest_list.pop(-1)
print(f"I am very sorry to inform you, {removed_guest.title()}, that I won't be able to invite you to the dinner.")

removed_guest = guest_list.pop(-1)
print(f"I am very sorry to inform you, {removed_guest.title()}, that I won't be able to invite you to the dinner.")

removed_guest = guest_list.pop(-1)
print(f"I am very sorry to inform you, {removed_guest.title()}, that I won't be able to invite you to the dinner.")

removed_guest = guest_list.pop(1)
print(f"I am very sorry to inform you, {removed_guest.title()}, that I won't be able to invite you to the dinner.")

print(f"\nThis is to inform that my {guest_list[0].title()} and {guest_list[1].title()} are still invited to the dinner tonight!! See ya!")
print("END\n")

# EMPTY THE LIST USING THE DEL FUNCTION
#del guest_list[1]
#del guest_list[0]
#print(f"Empty guest list: {guest_list}.") # Proving that the list is empty

# Use len() function to print number of people invited
print(f"The number of people I'm inviting are,", len(guest_list))