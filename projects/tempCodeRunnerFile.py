print("This is a Shopping list Manager, use it as you please. ")

s_list = []

while True: 
    action = input("What do you want to do with the item?\n   1. Add to list\n   2. Remove item in list\n   3. Show list\n   4. Quit\n   5. Mark Done\n ")

    if action == "1":
        item = input("What is the name of your item? \n").strip().lower().title()
        s_list.append(item)
        print(f"{item} is added to the list. ")
    elif action == "2":
        item = input("What is the name of your item? \n").strip().title()
        if item in s_list: 
           s_list.remove(item)
        else: 
           print("Try again")
    elif action == "3": 
        print(*s_list)
    elif action == "4": 
        print("So long cruel world!")
        break
    elif action == "5": 
        item = input("What is the name of your item? \n").strip().title()
        if item in s_list: 
            i = s_list.index(item)
            if " done" not in s_list[i]: 
                s_list[i] = item + " done"
                print('The deed is "done"')
            else:
                print("Item is already marked as done.")
        else: 
            print("Try Again")
    elif action == "Cave Story": 
        print("YOO!")
    else: 
        print("Sorry the number you have dialed does not exist, please try again\n")