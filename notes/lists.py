# BB 1st Lists Notes
import random

sibs = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jefferson", "Jake"] # Must have brackets, every item must be sepperated by a comma, every item in list must follow its data type (itself). 

print(*sibs)
print(sibs[0])
print(random.choice(sibs, weights=(10,20,10,10,10,10,20,10), k=8))
print(f"The list is {len(sibs)} people long")
sibs[0] = "Eric"
#sibs.replace("Katie", "Kathryn")
sibs[6:-1] = ["Xavier", "Hailey"]
sibs.pop()
sibs.pop(3)
sibs.remove("Andrew")
#sibs.clear()
#sibs.append("Andrew")
sibs.insert(2, "Andrew")
sibs.extend(["Joseph", "Israel", "Zee"])
print(sibs)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
        ]
fruit = ("Apple", "Orange", "Pineapple")#tuple ordered, not changeable

veggies = {"Spinach", "Kale", "Broccoli", "Carrot"}#Set unordered, changeable

print(veggies)
