# BB 1st Flexible Calculator Project
import flexible_calculator

kwarguments = []
kwarg = True
while kwarg: 
    kwargs = input("Which kwargument would you like to perform? ")
    print("\nEnter numbers (type 'done' when finished)")
    kwag = input("Number: ")
    if kwag == "Done":
        print("So long cruel world!")
        break
    elif kwag.isdigit(): 
        kwag = int(kwag)
    elif kwag.remove(".") == kwag.isdigit(): 
        kwag = float()
    else: print("Try again\n")



def id10t(): 
    num for num in kwarguments: 
