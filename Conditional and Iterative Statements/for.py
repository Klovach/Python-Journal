'''
For Loop:
A for loop is different from a while loop in that a for loop will execute a set number of times.
A for loop should be used when the number of iterations is known. The syntax for a for loop
in Python greatly differs from other languages.

for i in range(0, 10):
    #Do something.
'''

'''
Looping through Ranges:
Looping through a range of numbers from 0 to 10. Note that the range is exclusive of the last number. 
Tnerefore, the number 10 is not printed. Instead, 0 - 9 are printed.
'''
for x in range(0, 10):
    print(x)

# Looping through a list. 
donuts = ['chocolate', 'strawberry', 'vanilla', 'glazed', 'sprinkled']
for x in donuts:
    print(x)
    
 #Looping through a String.
for x in "George's Bakery":
    print(x)
    
# Looping through a Dictionary.
dictionary = {'name': 'George', 'age': 30, 'gender': 'Male', 'occupation': 'Baker'}
items = dictionary.items()
for key in dictionary:
    print(key, '->', dictionary[key]) # Prints key and values. 