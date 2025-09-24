# BB 1st Letter Grade Project
while True: 
    percent = int(input("What is your grade? \n".strip().strip("%")))
    if percent >= 94: 
        letter = "A"
    elif percent >= 90: 
        letter = "A-"
    elif percent >= 87: 
        letter = "B+"
    elif percent >= 84: 
        letter = "B"
    elif percent >= 80: 
        letter = "B-"
    elif percent >= 77: 
        letter = "C+"
    elif percent >= 74: 
        letter = "C"
    elif percent >= 70: 
        letter = "C-"
    elif percent >= 67: 
        letter = "D+"
    elif percent >= 64: 
        letter = "D"
    elif percent >= 60: 
        letter = "D-"
    else: 
        letter = "F"
    print(f"Your grade is a {letter}")

    again = input("Do you want to do another grade?\nY or N\n").strip().lower()

    if again == "y" or again == "yes" or again == "yus" or again == "yep": 
        pass
    else: 
        break