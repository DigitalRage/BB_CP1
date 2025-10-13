#BB 1st Password Strength Project
#https://www.geeksforgeeks.org/python/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/
#Added re (RegEx) module in order to fit all possible outcomes in smaller area and to return true or false since re.search Returns a Match object if there is a match anywhere in the string https://www.w3schools.com/python/python_regex.asp
import re
pwords = []
#loop that checks if there are 8 characters, lowercase, uppercase, numbers, & special characters
while True:
    #Variable is used to get the password and save it
    p_word = input("What is your password?\n").strip()
    pwords.append(p_word)

    #Holds the number for how string the password is
    strength = 5 

    #bool is used to return as true or false
    #re.search Returns a Match object if there is a match anywhere in the string
    #(r) is used to make sure that \ is not used as an excape character by turining it into a raw strint, hence r = raw
    #re.sa=earch allows to do first letter-last letter, making it easy to type it.
    #Variable to check if lowercase letters are there
    lowercase = bool(re.search(r'[a-z]', p_word))
    #Variable to check if uppercase letters are there
    uppercase = bool(re.search(r'[A-Z]', p_word))
    #Variable to check if numbers are there
    numbers = bool(re.search(r'[0-9]', p_word))
    #Variable to check if special characters are there
    special_char = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?~`]', p_word))

    #print(lowercase)
    #print(uppercase)
    #print(numbers)
    #print(special_char)
    #Previous lines are used to check if the variables are true or false

    #Main loop that checks if if there is sufficent passsword strength

    #Checks if there is 8 or more characters inside the password
    if len(p_word) < 8: 
        strength -= 1
        #this part updates that it is not sufficent and lowers password strength value (apply to next 4 loops)
        print("Password Length Unsufficent\n")
    else: 
        #this part updates that it is sufficent and keeps password strength as its current value (apply to next 4 loops)
        print("Password Length Sufficent\n")

    #Checks if there are uppercase letter(s) inside the password
    if uppercase == False: 
        strength -=1
        print("Password UpperCase Unsufficent\n")
    else: 
        print("Password UpperCase Sufficent\n")

    #Checks if there are lowercase letter(s) inside the password
    if lowercase == False: 
        strength -=1
        print("Password LowerCase Unsufficent\n")
    else: 
        print("Password LowerCase Sufficent\n")

    #Checks if there are number(s) inside the password
    if numbers == False: 
        strength -=1
        print("Password Digits Unsufficent\n")
    else: 
        print("Password Digits Sufficent\n")

    #Checks if there are special character(s) inside the password
    if special_char == False: 
        strength -=1
        print("Password Special Characters Unsufficent\n")
    else: 
        print("Password Special Characters Sufficent\n")

    #status bar that decreases by 20% for each missing feature
    if strength == 5: 
        #What it should show at 100% strength
        print("🟩🟩🟩🟩🟩100%\nVery Strong")
    elif strength == 4: 
        #What it should show at 80% strength
        print("🟩🟩🟩🟩🟥80%\nStrong")
    elif strength == 3: 
        #What it should show at 60% strength
        print("🟩🟩🟩🟥🟥60%\nModerate")
    elif strength == 2: 
        #What it should show at 40% strength
        print("🟩🟩🟥🟥🟥40%\nWeak")
    elif strength == 1: 
        #What it should show at 20% strength
        print("🟩🟥🟥🟥🟥20%\nWeak")
    elif strength == 0: 
        #What it should show at 0% strength
        print("🟥🟥🟥🟥🟥0%\nVery Weak")