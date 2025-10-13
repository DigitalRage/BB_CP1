#BB 1st Password Strength Project
import re#https://www.geeksforgeeks.org/python/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/

pwords = []

while True:
    p_word = input("What is your password?\n").strip()#This is to get the password

    pwords.append(p_word)

    strength = 5 #Holds the number for how string the password is

    lowercase = bool(re.search(r'[a-z]', p_word))#Used to check if lowercase letters are there
    uppercase = bool(re.search(r'[A-Z]', p_word))#Used to check if uppercase letters are there
    numbers = bool(re.search(r'[0-9]', p_word))#Used to check if numbers are there
    special_char = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?~`]', p_word))#Used to check if special characters are there

    #print(lowercase)
    #print(uppercase)
    #print(numbers)
    #print(special_char)
    #Previous lines are used to check if the variables are true or false

    if len(p_word) < 8: 
        strength -= 1
        print("Password Length Unsufficent\n")
    else: 
        print("Password Length Sufficent\n")

    if uppercase == False: 
        strength -=1
        print("Password UpperCase Unsufficent\n")
    else: 
        print("Password UpperCase Sufficent\n")

    if lowercase == False: 
        strength -=1
        print("Password LowerCase Unsufficent\n")
    else: 
        print("Password LowerCase Sufficent\n")

    if numbers == False: 
        strength -=1
        print("Password Digits Unsufficent\n")
    else: 
        print("Password Digits Sufficent\n")

    if special_char == False: 
        strength -=1
        print("Password Special Characters Unsufficent\n")
    else: 
        print("Password Special Characters Sufficent\n")

    if strength == 5: 
        print("🟩🟩🟩🟩🟩100%\nVery Strong")
    elif strength == 4: 
        print("🟩🟩🟩🟩🟥80%\nStrong")
    elif strength == 3: 
        print("🟩🟩🟩🟥🟥60%\nModerate")
    elif strength == 2: 
        print("🟩🟩🟥🟥🟥40%\nWeak")
    elif strength == 1: 
        print("🟩🟥🟥🟥🟥20%\nWeak")
    elif strength == 0: 
        print("🟥🟥🟥🟥🟥0%\nVery Weak")