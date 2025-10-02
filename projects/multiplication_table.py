# BB 1st Multplication Table Project
size = input("How long do you want the table? (must be at least 12)\n")
while size is not int: 
    try:
        size = int(size)
        if size < 12: 
            ValueError
        break
    except:
        size = input("That was not a valid number. How long do you want the table? (must be at least 12)\n")
print("test")

sizes = [size]

while True:
    if sizes[-1] > 0: 
        size = sizes[-1] - 1
        sizes.insert(0,size)
    else: 
        break
    print(sizes)