# Blaine Buckler 1st Who Are You? 
i = 0
while True: 
    names = []
    for i in range(1): 
        name = input("What is your name: ")
        names.append(name)

        colors = []
    for i in range(1): 
        color = input("What is your favorite color: ")
        colors.append(color)

    ages = []
    for i in range(1): 
        age = input("Please enter your age: ")
        ages.append(age)
        
    for name in names: 
        print("Hello", name + ". I see you like", color + ", INTERESTING...", "And your age is", age + ". I love", age, "year olds. ")