# sorting a list permanently with the sort() method
# sort() changes the order of the list to store the values alphabetically
# and the list can never be reverted to the original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sorting a list in reverse alphabetical order by passing the reverse=True argument 
# also permanent and cannot be reverted
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily in alphabetical order with the sorted() function
# lets you display your list in a particular order but doesn't affect the actual order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# printing a list in reverse order, does not sort alphabetically, only reverses
# changes the order of a list permanently but can be reverted using reverse() a second time
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# finding the length of a list using the len() function
# Python counts the items in a list starting with one (as opposed to indexing)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))