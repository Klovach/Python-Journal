'''
List Slices:
List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list 
with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
'''
numbers = list(range(5, 10, 2))
print(numbers)

# This list contains the numbers 1 through 10. 
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:5]) # Prints the first five items in the list.
print(list[5:10]) # Prints the last five items in the list.

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

# If the first number in a slice is omitted, it is taken to be the start of the list.
print(list[:5])
# If the second number is omitted, it is taken to be the end.   
print(list[5:])
# Range slices can include a third number to represent a step.
print(list[1:10:2]) 

# Negative numbers can be used in list slicing (and normal list indexing). Here, a negative number is utilized to reverse the list. 
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res) 


list = [1, 1, 2, 3, 5, 8, 13]

print(list[list[4]])
