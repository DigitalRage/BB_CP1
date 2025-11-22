#BB 1st Factorial Calculator Pseudo Code Project

#!!! is added before new lines of pseudo code
#def can_int(user_inp): 
#    try to change user_inp to int, return true 
#    except: return False
#
#def factor(user_inp): 
#    !!! set result = 1
#    !!! for i in range(user_inp down to 1): 
#    !!!     result = result * i
#    !!! return result
#
#print instructions for inputting a number
#while True: 
#    user_num = input()
#    if can_int(user_num) is True: 
#        break from loop
#    else: 
#        print that their input was not valid and to try again
#
#!!! print the multiplication steps (e.g. "5 × 4 × 3 × 2 × 1 = 120")

def can_int(user_inp):
    try:
        int(user_inp)
        return True
    except:
        return False

def factor(user_inp):
    result = 1
    steps = []
    for i in range(user_inp, 0, -1):
        result *= i
        steps.append(str(i))
    if user_inp == 0:
        return "0! = 1"
    return " × ".join(steps) + " = " + str(result)

print("What number do you want the factorial of:")
while True:
    user_num = input()
    if can_int(user_num):
        user_num = int(user_num)
        break
    else:
        print("Input was not valid, try again")

print(factor(user_num))