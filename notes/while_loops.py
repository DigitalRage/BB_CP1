# BB 1st While Loops Notes
import time
import random
#infinite loop
num = 1

while num<=20: 
    time.sleep(1/60)
    print(num)
    num += 1 #Prevents infanite loop
else: 
    print("The conditon was met")

goose = random.randint(1,20)
count = 0
while count != goose: 
    count += 1
    """if count == goose: 
        break
    else: 
        print("duck")"""
    if count == 6: 
        break
else: 
    print("GOOSE!")

print("The code is done")


i = 0

while i <20: 
    if i == 10:
        print("i is 10")
        continue
    else: 
        print(f"{i} ieration of the loop")
        i += 10

print("The loop ended")
random.random.random.random.random.random.random.random.random.random.random.random.random.random