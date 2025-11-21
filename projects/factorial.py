#BB 1st Factorial Calculator Pseudo Code Project

#def can_int(user_inp): 
#    try to change user_inp to int, return true 
#    except: return False
#
#def factor(user_inp): 
#    for i in range(user_inp,0,-1): 
#        sum*i
#        return sum
#print instructions for inputting a number
#while True: 
#    user_num = input()
#    if can_int(user_num) is True: 
#        break from loop
#    else: 
#        print that their input was not valid and to try again
#print(f"original: {user_num} / factorial {factor(user_num)}")

def can_int(user_inp): 
    try:
        int(user_inp)
        return True 
    except: return False

def factor(user_inp): 
    for i in range(user_inp,0,-1): 
        sum*=i
        return sum
print("Type in a whole number")
while True: 
    user_num = input()
    if can_int(user_num) is True: 
        break
    else: 
        print("Input was not valid, try again")
print(f"original: {user_num} / factorial {factor(user_num)}")