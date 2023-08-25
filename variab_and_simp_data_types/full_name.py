# using f-strings to display multiple variables
# prints both the first name and the last name
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# using f-strings inside a print statement to compose complete messages using information
# associated with a variable
# prints hello with the first name and the last name 
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# using f-strings to compose a message, and then assign the entire message to a variable
# prints the message
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)