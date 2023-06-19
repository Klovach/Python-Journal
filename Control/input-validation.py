import re
'''
Input Validation:
This journal entry is a personal resource for input validation.
This entry contains "valid password", "valid name", "valid age" functions, and more.
'''

# Valid Name Function
def valid_name(name):
    if len(name) < 6 or len(name) > 20:
        return False
    else:
        return True
    
# Valid Password Function
def strong_password(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_char = any(char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 " for char in password)
    length = len(password)

    if has_lower and has_upper and has_digit and special_char and length >= 8:
        strength = "Strong"
        print("Strength of password: " + strength)
        return True
    elif (has_lower or has_upper) and special_char and length >= 6:
        strength = "Moderate"
        print("Strength of password: " + strength)
        return False 
    else:
        strength = "Weak"
        print("Strength of password: " + strength)
        return False
    

# Valid Age Function
def valid_age(age):
    try:
        if age < 0 or age > 120:
            return False
        else:
            return True
    except ValueError:
        return False
    
# Valid Email Function
def valid_email(s):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern,s):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False 
    
# Driver code
valid_input = False
while not valid_input:
    name = input("Enter name: ")
    if valid_name(name):
        valid_input = True
    else:
        print("Invalid name. Name should be between 6 and 20 characters.")

valid_input = False

while not valid_input:
    password = input("Enter password: ")
    if strong_password(password):
        valid_input = True
    else:
        print("Weak or moderate password. A strong password should have at least 8 characters and contain a combination of lowercase letters, uppercase letters, digits, and special characters.")

valid_input = False

while not valid_input:
    age = int(input("Enter age: "))
    if valid_age(age):
        valid_input = True
    else:
        print("Invalid age. Age should be a number between 0 and 120.")

valid_input = False

while not valid_input:
    email = input("Enter email: ")
    if valid_email(email):
        valid_input = True
    else:
        print("Invalid email. Please enter a valid email address.")

print("You have successfully registered! Here is your information:")
print("Name:", name)
print("Password:", password)
print("Age:", age)
print("Email:", email)