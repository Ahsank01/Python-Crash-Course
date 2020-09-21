# Name: Ahsan Khan
# Date: 09/15/2020
# Description: Using string and its built-in functions, and manipulating the string.

# the function .title() will make the first initial a capital letter
name = "ahsan khan"
print(name.title())

#------------------------------------------------------------------#

# the function .upper() will make the whole string an uppercase string
# the function .lower() will make the whole struing a lowercase string
print(name.upper())
print(name.lower())

#------------------------------------------------------------------#

# f-string is for formatting the data.
first_name = "ahsan"
last_name = "khan"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

#------------------------------------------------------------------#

# the function .rstrip() will erase all the useless whitespace from the right side
# the function .lstrip() will erase all the useless whitespace from the left side 
# the function .strip() will erase all the useless whitespace from the left and right side
message = "ahsan "
print(f"'{message}'")
message = message.rstrip()
print(f"'{message}'")

message = " ahsan"
print(f"'{message}'")
message = message.lstrip()
print(f"'{message}'")

message = " ahsan "
print(f"'{message}'")
print(f"'{message.strip()}'")
