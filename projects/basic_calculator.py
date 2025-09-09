# BB 1st Basic Calculator Project
while True:

    num1 = input("Please type number: ")
    num2 = input("Please type another number: ")

    i = input("Please select one of the options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Integer Division\n6. Modulo\n7. Exponent\n Type Here: ")
    if i.isdigit() and num1.replace(".","",1).replace("-","",1).isdigit() and num2.replace(".","",1).replace("-","",1).isdigit():
        i = int(i)

        num1 = float(num1)
        num2 = float(num2)

        if i == 1:
            add = num1 + num2
            print(f"{num1:.2f}+{num2:.2f}={add:.2f}")

        elif i == 2: 
            subtract = num1 - num2
            print(f"{num1:.2f}-{num2:.2f}={subtract:.2f}")

        elif i == 3: 
            multiply = num1 * num2
            print(f"{num1:.2f}*{num2:.2f}={multiply:.2f}")

        elif i == 4: 
            divide = num1 / num2
            print(f"{num1:.2f}/{num2:.2f}={divide:.2f}")
            
        elif i == 5: 
            idivide = num1 // num2
            print(f"{num1:.2f}//{num2:.2f}={idivide:.2f}")

        elif i == 6: 
            mod = num1 % num2
            print(f"{num1:.2f}%{num2:.2f}={mod:.2f}")

        elif i == 7: 
            exponent = num1 ** num2
            print(f"{num1:.2f}**{num2:.2f}={exponent:.2f}")
        else: print("Try Again")
    else: print("Try Again")