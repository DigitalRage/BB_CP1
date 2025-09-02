# BB 1st Strings Notes

#balance = 1000

#print("Balances: " + str(balance))

#balance += 200

#print("Balances: " + str(balance))

#What is a string
#A collection of symbols held together by quotation marks. 
#"Content in String"


#String Examples: 
setence = "The quick brown fox jumps over the lazy job!"
first_name = "Tia"
month = "September"
book = "The Return of the King"
food = "Chocolate"

print(setence)
length = len(setence)
print(len(setence))
print ("The sentence is", length, "characters long")

print('"Inkheart"is the best book ever')
print("\t'Inkheart'is the best book ever")


# Escape Characters

print("\"Inkheart\"is the best book\never")



#Concatenation
#To put two strings together (only strings, no space in between)
#string_one + string_two
last_name = "LaRose"
full_name = first_name + " " + last_name
print(full_name)

#index
print(last_name[:2])
print(setence[10:15])