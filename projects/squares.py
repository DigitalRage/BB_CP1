#BB 1st Square Numbers Project
#for i in range(1,20):print(f'Original:{i},Squared:{i*i}') #57 Characters Golfed
numbers = range(1,20)
squares = map(lambda x: x*x, range(1,20))
for square in squares:
    for number in numbers:
        if square == number * number:
            print(f'Original:{number},Squared:{square}') #203 Characters UnGolfed