'''
Lists:
Lists are used to store multiple items in a single variable.
In Python lists are written with square brackets. Lists are mutable, meaning that they can be changed.
'''

# Initializing a list
flavor_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] # String List
numbers_list = [1, 2, 3, 4, 5, 6, 7] # Integer List
validity_list = [True, False, False, True] # Boolean List

# Sorting a list alphabetically
list.sort(flavor_list)
# Sorting a list  numerically.
list.sort(numbers_list)

# Iterating through a list.
for x in flavor_list:
    print(x)

for x in numbers_list:
    print(x)
    
# Accessing items in a list.
print(validity_list[0]) # Prints the first item in the list.
print(validity_list[1]) # Prints the second item in the list.
print(validity_list[-1]) # Prints the last item in the list.

# Changing items in a list.
flavor_list[0] = "strawberry"


# Iterating through a list in reverse order. 
list.sort(flavor_list)
for x in reversed(flavor_list):
    print(x)