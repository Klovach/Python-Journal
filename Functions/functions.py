'''
Functions:
A function is a block of code that performs a specific task. Functions serve an important role in code modularization. 
Functions can be reused in different parts of a program. A function has a name and arguments. In Python, there are many
built-in functions. For example, print, range, and str are all functions which take arguments and perform a specific task. 
Functions can have multiple arguments. Functions can also return a value. The return statement is used 
to return a value from a function.
'''

# Basic Function
def hello():
   print("Hello world!")
 
def hello_user(name):
    print("Hello " + name + "!")
    
 # Function with arguments
def add(x, y):
   return x + y

# Function with list argument
def list_function(list):
   for x in list:
       print(x)

books = ["Harry Potter", "Lord of the Rings", "Winnie the Pooh"]
list_function(books)

# Recursion
def recursion(n):
   if n == 1:
       return 1
   else:
       return n * recursion(n-1)

# Driver Code 
hello() 
print("Enter your name: ")
name = (input())
hello_user(name)
print(add(2,3))
list_function(books)
print(recursion(5))