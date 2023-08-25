print("Python")
# use \t to add a tab to the text
print("\tPython")

# use \n to add a newline in a string
print("Languages:\nPython\nC\nJavaScript")

# combining tabs and newlines in a single string
print("Languages:\n\tPython\n\tC\n\tJaveScript")

# the following lines of code work only in the terminal, not in the editor

# to ensure no whitespace exists at the right end of a string, use the rstrip() method
favorite_language = 'python '
# prints 'python ' in terminal
favorite_language
# prints 'python' in terminal 
favorite_language.rstrip()
# still prints 'python ' in terminal. to remove permanently, see next code block
favorite_language

# to remove whitespace from the string permanently, associate the stripped value with the variable name
favorite_language = 'python '
favorite_language = favorite_language.strip()
# prints 'python' in the terminal
favorite_language

# strip whitespace from the left side of a string using lstrip() method, or from both sides at once 
# using strip()
favorite_language = ' python '
# strips the right side and prints ' python' in the terminal
favorite_language.rstrip()
# strips the left side and prints 'python ' in the terminal
favorite_language.lstrip()
# strips both sides at once and prints 'python' in the terminal 
favorite_language.strip()

# in the real world, these stripping functions are used most often to clean up user input before it's
# stored in a program