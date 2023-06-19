'''
do-while:
This journal entry examines emulating do-while loops in Python.
A do-while loop is a control flow statement that executes a block of code at least once, and then repeatedly executes 
the block  depending upon a given boolean condition at the end of the block. To emulate a do while loop,
we can use an infinite while loop and a break statement. The break statement is used to exit a loop prematurely.

while True:
    #Do something. 
    if condition:
        break
'''

#Do While Loop Example
while True:
    number = int(input("Enter an even number: "))
    if number % 2 != 0:
        print("Your number was not even: " + str(number))
    if number % 2 == 0:
        break
    

