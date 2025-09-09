# BB 1st Basic Calculator Project
while True:

    num1 = float(input("Please type number: "))
    num2 = float(input("Please type another number: "))

    i = input("Please select one of the options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Integer Division\n6. Modulo\n7. Exponent")
    if i.isdigit():
        i = int(i)

        if i == 1:
            add = num1 + num2
            print(f"{num1}+{num2}={add}")

        elif i == 2: 
            subtract = num1 - num2
            print(f"{num1}-{num2}={add}")

        elif i == 3: 
            multiply = num1 * num2
            print(f"{num1}*{num2}={add}")

        elif i == 4: 
            divide = num1 / num2
            print(f"{num1}/{num2}={add}")
            
        elif i == 5: 
            idivide = num1 // num2
            print(f"{num1}//{num2}={add}")

        elif i == 6: 
            mod = num1 % num2
            print(f"{num1}%{num2}={add}")

        elif i == 7: 
            exponent = num1 ** num2
            print(f"{num1}**{num2}={add}")
        else: print("Try Again")
    else: print("Try Again")