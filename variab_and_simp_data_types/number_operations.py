# Integers
# add +
print(2 + 3)

# subtract -
print(3 - 2)

# multiply * 
print(2 * 3)

# divide /
print(3 / 2)

# exponents **
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

# order of operations and using parentheses to modify the order of operations
print(2 + 3 * 4)
print((2 + 3) * 4)

# Floats, numbers with a decimal point
# adding floats
print(0.1 + 0.1)
print(0.2 + 0.2)

# multipying floats
print(2 * 0.1)
print(2 * 0.2)

# be aware that you can sometimes get an arbitrary number of decimal places 
# both of the following print statements outputs 0.30000000000000004 instead of 
# the expected 0.3
print(0.2 + 0.1)
print(3 * 0.1)

# Integers and Floats
# when you divide any two numbers, even if they are integers that result in a whole
# number you'll always get a float
print(4 / 2)

# mixing integers and floats in any other operation also results in a float
# Python defaults to float in any operation that uses a float 
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

# when writing long numbers, digits can be grouped using underscores for better readability
universe_age = 14_000_000_000
# using the print() function, Python prints only the digits
print(universe_age)

# assigning values to more than one variable using just a single line of code
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
print(x, y, z)

# a constant is like a variable whose value stays the same throughout the life of a program
# Python doesn't have built-in constant types but when you want to treat a variable as a constant
# make the name of the variable all capital letters
MAX_CONNECTIONS = 5000