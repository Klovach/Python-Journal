'''
Casting:
This is a journal entry regarding the subject of casting. This entry demonstrates
how to assign values to multiple variables, display variable types, and change
variable types at will. There are some circumstances in which we may want to change a variable's type.
A common usage of casting is altering the variable type of user input.
'''

# First, we will assign values to multiple variables.
x, y, z = (1, 2.5, 4.4)

# Print Types
print(type(x), x) # Type of x
print(type(y), y) # Type of y
print(type(z), z) # Type of z

# Type Casting 
x = str(x)
y = int(y)
z = str(z)

# Print Values
print(x, y, z)

# Print Types
print(type(x), x) # Type of x
print(type(y), y) # Type of y
print(type(z), z) # Type of z
