'''
Emulating Switch Cases:
    - Python does not have a switch statement
    Unlike every other language, Python does not have a switch statement. 
    To emulate a switch statement in python we can use a dictionary.
    A dictionary is a data structure that maps keys to values. In python, a dictionary is defined using curly braces.
    In Python 3.10 and beyond, we can also use match-case statements to emulate switch cases.
'''

# Match Case Approach
def match_case_example(season):
    match season:
        case "Spring":
            print("Warm")
        case "Summer":
            print("Hot")
        case "Fall":
            print("Cool")
        case "Winter":
            print("Cold")


# Dictionary Approach
def dictionary_approach(season):
    switcher = { 
        "Spring": "Warm",
        "Summer": "Hot",
        "Fall": "Cool",
        "Winter": "Cold"
    }
    print(switcher.get(season, "Invalid Season"))