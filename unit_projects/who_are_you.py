# Blaine Buckler 1st Who Are You? 
i = 0
names = []
colors = []
ages = []

while True: 
    name = input("What is your name: ")
    
    if name in names: 
        position = names.index(name)
        
        print(f"Hello {name}. I see you like {colors[position]}, INTERESTING... And your age is {ages[position]}. I love {ages[position]} year olds. ")
    else:
        names.append(name)
        
        color = input("What is your favorite color: ")
        colors.append(color)
        
        age = input("Please enter your age: ")
        ages.append(age)
            
        print(f"Hello {name}. I see you like {color}, INTERESTING... And your age is {age}. I love {age} year olds. ")