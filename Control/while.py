'''
While Loop:
This is a simple while loop in its most simple form. 
A while loop is different from a for loop in that a for loop will execute a set number of times, 
while a while loop will execute until a condition is met. A while loop should be used when the number of iterations is unknown.

while condition:
    #Do something.
'''
example = 3
while example > 0:
    print("While Loop Example " + str(example) + "!")
    example -= 1

'''
Odd or Even:
One way to determine whether or not
a number is odd or even is to use x%2 == 0 or x%2 != 00. This expression means this:
If the number, x, has a reminder of zero when divided by two the number is even.
If it does not, the number is odd. It should be noted this snippet could have also been written with
a for loop. 
'''
x = 1
while x <= 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

'''
Continue and Break:
Continue and break are important for control. A common use for these is input 
validation. For example, you might use break and continue to ensure a while
loop does not cease until it acquires a correct answer from a user. 

This snippet gathers the ages of five people and outputs the total of all of
their tickets. Each ticket is 100 dollars. If the person is under three
years old, they are not charged. 
'''

total = 0.0
i = 0
while True:
    age = int(input())
    if (age > 3):
        total += 100; #Add 100 to the total. 
    i = i + 1
    if (age < 3):
        continue #Jump back to the beginning of the loop. 
    if i >= 5:
        break #Break the loop. 

print(total) #End of the loop, print the total. 