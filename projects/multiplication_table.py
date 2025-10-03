# BB 1st Multplication Table Project
length = int(input("How big?\n").strip())
list = []
while True: 
    if length >= 12: 
        for len in range(length): 
            list.append(len+1)
        for x in list: 
            for y in list: 
                print(x*y, end =" ")
            print()
        break
    else: 
        print("Try Again")
        continue