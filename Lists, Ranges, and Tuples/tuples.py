'''
Tuples:
Tuples are immutable. Unlike lists, tuples cannot be changed.
'''
menu = ("spam", "eggs", "sausages")
print(menu[0])

# Usage of tuples in a for loop and list.
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()
# Find the first occurence of a list item and return its index
for item in contacts:
    if name in item:
        print(str(item[0]) + " is " + str(item[1])) 
        break
else:
    print("Not Found")