'''
Lambda Functions:
Lambda functions are useful for creating quick functions that are not needed elsewhere in the code.
The syntax for a lambda function is: lambda arguments: expression. 
Below are some examples of lambda functions.

lambda keyword  - A keyword that is used to define a lambda function.
arguments - Input parameters or arguments for the function. 
expression -  The single-line code to be executed and the value to be returned.
'''

# Lambda Function Example:
# Here, num is the argument and x * x is the expression.
square = lambda num: num * num  

# Here are some other examples.
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

result = square(5)
sum = add (5, 2)
difference = subtract(5, 2)
product = multiply(5, 2)
div = divide(10, 2)

print(result)
print (sum)
print (difference)
print (product)
print (div)