# it's a good idea to make the name of your list plural because lists usually contain more than one element
# in Python, square brackets [] indicate a list and individual elements are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# when printing, Python returns the list's representation including the square brackets
print(bicycles)

# to access any element in a list by writing the name of the list followed by the index of the item
# accessing the first bicycle in the list of bicycles and Python returns only that element without
# square brackets 
print(bicycles[0])

# formatting the element by using the title() method
print(bicycles[0].title())

# index positions start at 0
# the following asks for the bicycles at index 1 and index 3 and returns the 2nd and 4th bicycles in the list
print(bicycles[1])
print(bicycles[3])

# the last item in a list can be accessed by using index -1 
print(bicycles[-1])
# extends to other negative index values. index -2 returns the second item from the end of the list 
print(bicycles[-2])
# and index -3 returns the third item from the end of the list, etc.
print(bicycles[-3])

# using f-strings to create a message based on a value from the list
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)