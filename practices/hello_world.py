# Blaine Buckler 1st Hello World 
names = []
for i in range(5): 
    name = input(f"Please enter name #{i+1}: ")
    names.append(name)

for name in names: 
    if name in ["Ms. Larose", "Vienna Larose", "Vienna"]: 
        print("Hello Ms. Larose and welcome to the classroom. ")
    elif name in ["Blaine", "Blaine Buckler"]:
        print("Hello my creator")
    else: 
        print("Hello", name + ". I hope you are having a great day! ")