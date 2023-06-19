'''
If, Else, and Elif:
Understanding the if, else, and elif statements is crucial to understanding how to control the flow of a program.
Unlike other languages, indentations are used to denote code blocks instead of curly braces or other symbols.
Below are some usage cases for if, else, and elif statements.
    - If: If the condition is true, then the code will be executed.
    - Elif: If the condition is true, then the code will be executed.
    - Else: If the condition is false, then the code will be executed.
'''

# BMI Calculator Example
weight = 120.0
height = 5.9
bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
    
    
# Age Example
age = 18

if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult") 
else:
    print("Senior")