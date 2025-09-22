# BB 1st User Sign In Project

names = []
passwords = []


while True: 
    name = input("What is your username?\n").strip()
    password = input("What is your Password, Gime it!\n").strip()

    if name in names: 
        position = names.index(name)
        if passwords[position] == password: 
            print(f"Hello {names[position]}. Your username and password looks right.")
        else: 
            print("Wrong password try again. ")
    elif name and password: 
        names.append(name)
        passwords.append(password)
        print("Yo, you have a valid username and password!!!")
    elif not password:
        print("Type something for your pasword you dingus")
    else: 
        print("JUST TYPE SOMETHING!!!")
        