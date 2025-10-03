import random
comp = random.choice(["rock","paper","scisor"])
choice = input("What do you chose (R,P,S)").strip().lower()
while choice != "r" or choice != "p" or choice != "s": 
    print("Try Again")
    