# BB 1st Order Up! Project
mainFood = {
    "Burger":{
        "HoomBurger": 10.00, 
        "CheeseBurger": 10.00, 
        "BigMacWhoper": 10.00, 
        "Double Double Chris Pratt Style": 10.00
    }, 
    "Mac and Cheese": {
        "Chinese Mac and Cheese": 10.00, 
        "Mexican Mac and Cheese": 10.00, 
        "American Mac and Cheese": 1000.00
    }, 
    "Tacos": {
        "Soft Tacos": 0.01, 
        "Street Tacos": 10.00, 
        "Delt Tacos": 1000.00
    }
}
drink =  {
    "Milkshakes": {
        "Chocolate Milkshake": 10.00, 
        "Vanilla Milkshake": 10.00, 
        "StrwBerry Milkshake": 10.00, 
        "The Mystery Milkshack": 1000.00
    },
    "Watter": {
        "Tap-Water": 100.00, 
        "Fresh Water": 1000.00
    }, 
    "Geuse": {
        "Aypell Geuse": 10.00, 
        "Aaronge Geuse": 10.00, 
        "BeetleGeuse": 100000.00
    }
}
sides = {
    "Mashed Potatoes": 10.00, 
    "1000lb Fry": 0.01, 
    "Salid": 1000000.00, 
    "Bread": 10.00, 
    "Onion Rings": 10.00
}

print(f"\nMain Course")

for outsideKey, stuff in mainFood.items(): 
    print(f"\n{outsideKey}\n")
    for insideKey, insideValue in stuff.items(): 
        print(f"{insideKey}::::::::::{insideValue}")

print(f"\nDrinks")

for outsideKey, stuff in drink.items(): 
    print(f"\n{outsideKey}\n")
    for insideKey, insideValue in stuff.items(): 
        print(f"{insideKey}::::::::::{insideValue}")

print(f"\nSides\n(Get at least 2 or die)")

for key in sides.keys(): 
    print(f"{key}::::::::::{sides[key]}")