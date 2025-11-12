# BB 1st period, Dictionaries Notes! 
avatar = {
    "earth": {
        "Toph": "Sounds like Tough and thats what I am (not)"
    }, 
    "water": {
        "Katara": "It game me so much HOPE!", 
        "Sokka": "I used to be boomerang guy."
    },
}
print(avatar["earth"]["Toph"])

person = {
    #key:value, 
    "name": "Xavier",
    "age": 22,
    "job": "Maverik",
    "sibling": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"]
}
person_two = {
    "name": "Jake",
    "age": 21,
    "job": "NEET",
    "sibling": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier"]
}


print(person["name"])
print(person["sibling"][3])
person_two['age'] += 1
print(person.keys())

for key in person.keys(): 
    if key == "sibling": 
        for name in person[key]: 
            print(f"{person['name']} has siblings named {name}")
    else: 
        print(f"{key} is {person[key]}")