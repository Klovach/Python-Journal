'''
String Functions:
Below is a list of relevant string functions.
len(string): Returns the length of a string.
format(): Formats a string.
joint(): Joins a list of strings with another string as a separator.
split(): Splits a string into a list of strings.
string.count(substring): Returns the number of times a substring occurs in a string.
string.upper(): Returns a copy of the string with all characters uppercased.
string.lower(): Returns a copy of the string with all characters lowercased.
'''

# Format
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# Join
x = ", ".join(["spam", "eggs", "ham"])
print(x)

# Split
str = "some text goes here"
x = str.split(' ')
print(x)

# Replace
str = "Hello World"
print(str.replace("World", "Universe"))
msg = "BROKEN#MESSAGE#HERE"
print(msg.replace("#", " "))

# Upper & Lower Case 
print(str.upper())
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())