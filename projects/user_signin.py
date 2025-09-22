# BB 1st User Sign In Project

names = []
paswords = []


while True: 
    name = input("What is your username?\n").strip
    password = input("What is your Password, Gime it!\n").strip

    if name in names and name == True: 
        position = names.index(name)
        print(f"Hello {name[position]}. Your username and password looks right.")
    elif name == True: 
        if password == True: 
            print("Yo, you have a valid username andpassword!!!")
        else:
            print("Type something for your pasword you dingus")
    else: 
        print("JUST TYPE SOMETHING!!!")
    
    
        
"""    else:
        names.append(name)
        
        color = input("What is your favorite color: ")
        colors.append(color)
        
        age = input("Please enter your age: ")
        ages.append(age)
            
        print(f"Hello {name}. I see you like {color}, INTERESTING... And your age is {age}. I love {age} year olds. ")"""