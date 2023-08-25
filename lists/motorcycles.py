# modifying elements in a list
# to change an element, use the name of the list followed by the index of the element
# you want to change, and then provide the new value you want that item to have
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changing the value of the first item, removes 'honda' and replaces it with 'ducati'
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
# the simplest way to add a new element to a list is to append the item to the list
# when you append the new item is added to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# appending 'ducati', appending an item adds the item to the end of the list without 
# affecting any of the other elements in the list 
motorcycles.append('ducati')
print(motorcycles)

# the append() method makes it easy to build lists dynamically. 
# using an empty list and adding elements using a series of append() calls
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements into a list
# specify the index of the new element and the value of the new item to add 
# a new element at any position in a list by using insert()
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing an item using the del statement
# if you know the index of the item you want to remove, you can use the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# using del to remove the second item, 'yamaha'
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# removing an item using the pop() method
# the pop() method removes the  last item in a list, but it lets you work with that 
# item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# as an example of how the pop() method can be useful
# imagine that the motorcycles in the list are stored in chronological order according 
# to when it was owned. the pop() method can be used to print a statement about the 
# last motorcycle that was bought
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# popping items from any position in a list
# use pop() to remove an item from any position by including the index of the item 
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# when you want to delete an item from a list and not use that item in any way, 
# use the del statement
# when you want to use an item as you remove it, use the pop() method

# removing an item by value 
# if you only know the value of the item you want to remove, you can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# using remove() method to work with a value that's being removed from a list
# removing the value 'ducati' and printing the reason for removal
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")