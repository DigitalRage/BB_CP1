#BB 1st *Args & **Kwargs Notes

def hellos(name='tia',age=29): 
    return f"hello {name}! You are {age}"

print(hellos())
print(hellos("Treyson",19))
print(hellos("Vienna"))
print(hellos(age=37))

def hello(*names, **kwargs): 
    print(type(names))
    print(kwargs)
    for n in names: 
        print(f"Hello {n} {kwargs['last_name']}")

hello("Mat","Yes","chris",last_name="id10t",dad="idiot",num_cats=5)

def full_name(**names): 
    if'middle'in names.keys(): 
        return f"{names['first']}{names['middle']}{names['last']}"
    else: 
        return f"{names['first']}{names['last']}"
    
print(full_name(age="???",first="yes",last="no"))
print(full_name(age="so old",first="yes",middle="maby",last="no"))

def summary(**story): 
    sum = ""
    if "name" in story.keys(): 
        sum+=f"{story['name']} is the main character of this story."
    if "place" in story.keys(): 
        sum+=f"The story takes places in {story['place']}"
    if "conflict" in story.keys(): 
        sum+= f"The problem is {story['conflict']}"

    return sum

print(summary(name = "Luke Skywalker", place= "A galaxy far far away"))
print(summary(name = "Harry Potter", conflict= "Yes"))