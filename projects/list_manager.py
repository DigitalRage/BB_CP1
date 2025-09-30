# BB 1st Shopping List Manager
print("This is a Shopping List Manager, use it as you please. ")

list = []

while True: 
    action = input("What do you want to do with the item?\n   1. Add to list\n   2. Remove item in list\n   3. Show List\n   4. Quit\n   5. Mark Done\n ")

    if action == "1":
        item = input("What is the name of your item? \n").strip()
        list.append(item + "\n")
    elif action == "2":
        item = input("What is the name of your item? \n").strip()
        if item in list: 
           list.remove(item)
        else: 
           print("Try again")
    elif action == "3": 
        print(*list)
    elif action == "4": 
        print("So long cruel world!")
        break
    elif action == "5": 
        
    elif action == "Cave Story": 
        print("YOO!")
    else: 
        print("Sorry the number you have dialed does not exist, please try again\n")