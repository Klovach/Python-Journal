'''
List Functions:
There are several functions that can be used to manipulate lists.

len(list): Returns the number of items in a list.
list.append(item): Adds an item to the end of a list.
list.insert(index, item): Inserts an item at a given position.
list.count(item): Returns a count of how many times an item occurs in a list.
list.remove(item): Removes an item from a list.
list.reverse(): Reverses items in a list.
'''

# Get length of a list
nums = [1, 2, 3, 4, 5]
print(len(nums))
# Use len on a string to get the length of its character count.
string = "Hello"
print(len(string))

# Append an item to the end of a list
nums.append(6)

# Insert an item at a given position. The first argument is the index of the element before which to insert.
words = ["Journaling", "productive"]
words.insert(1, "is")
print(words)

# Find the first occurence of a list item and return its index
print(nums.index(3)) 

# Return the maximum value or the minimum value in a list. 
print(min(nums))
print(max(nums))


# Count the number of times an item appears in a list.
print(nums.count(2))

# Remove an item from a list.
nums.remove(4)
print(nums)

# Reverse the order of items in a list.
nums.reverse()
print(nums)