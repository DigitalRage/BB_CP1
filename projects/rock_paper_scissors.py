# BB 1st Rock Paper Scissors Project
import random

ur_num = 0
comp_num = 0

while True: 
    comp = random.choice(["rock","paper","scissor"])
    choice = input("What do you chose (Rock,Paper,Scissors)").strip().lower()
    if choice != "rock" and choice != "paper" and choice != "scissor": 
        print("Try Again")
        continue
    else:
        pass


    if choice == "rock": 
        if comp == "rock": 
            print("You Tied")
        elif comp == "paper": 
            print("You Lost")
            comp_num +=1
        else: 
            print("You Won")
            ur_num +=1
    elif choice == "paper": 
        if comp == "paper": 
            print("You Tied")
        elif comp == "scissor": 
            print("You Lost")
            comp_num +=1
        else: 
            print("You Won")
            ur_num +=1
    elif choice == "scissor": 
        if comp == "scissor": 
            print("You Tied")
        elif comp == "rock": 
            print("You Lost")
            comp_num +=1
        else: 
            print("You Won")
            ur_num +=1
    else: 
        print("This shouldn't have happened dingus. ")
    print(f"Your score: {ur_num}\nComputer score: {comp_num}")