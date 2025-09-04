# BB 1st String Methods Notes

#subject = "Computer Programming 1!"

#print(subject.upper())
#print(subject.upper())
#print(subject.lower())
#print(subject.center(100))
#print(subject)
#print(subject)
#print(subject)
#print(subject)

# stupid/idiot proofing inputs
#color = input("What is your favorite color?").strip().lower().capitalize()
#lower() => all lowercase
#upper() => all uppercase
#capitalize() => Capitalize the first letter of the first word
#title +> Capitalize the first letter of eacth word
#full_name = input("WHat is your full name?").strip().title()
#print("That is cool" + full_name + ". I like " + color + " too!")
#print("That is cool {full_name}. I like {color} too!".format(full_name=full_name, color=color))

#f-strings
#print(f"That is cool {full_name}. I like {color} too!")

#pi = "3.14159"
#print(f"We all know pi is equal to {pi:.3f}")
#print(pi.isdigit())
#print(pi.isdecimal())

setence = "The quick brown fox jumps over the lazy dog!"
word = "jumps"
print(setence.find(word))
start = setence.index(word)
length = len(word)
print(setence[start:start+length])
print(setence.replace(word, "swims"))
print(setence)