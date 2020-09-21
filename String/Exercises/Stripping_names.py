# Name: Ahsan Khan
# Date: 09/15/2020
# Description: Strip the whitespace from the data.

name = "\t  Ahsan Khan  \n"
print(f"'{name}'")

# Remove whitespace from the right side
name = name.rstrip()
print(f"'{name}'")

# Remove whitespace from the left side
name = name.lstrip()
print(f"'{name}'")

# Remove whitespace from all the sides
name = "\t\t    ahsan khan   \n\n"
print(f"'{name}'")
print(f"'{name.strip()}'")