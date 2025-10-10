#BB 1st Password Strength Project
import re#https://www.geeksforgeeks.org/python/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/

p_word = input("What is your password?\n").strip()#This is to get the password

strength = 5 #Holds the number for how string the password is

lowercase = bool(re.search(r'[a-z]', p_word))
uppercase = bool(re.search(r'[A-Z]', p_word))


print(lowercase)
print(uppercase)

numbers = [1,2,3,4,5,6,7,8,9,0]
letters = ['q','w','e','r','t','y','u','i',]

if len(p_word) < 8: 
    strength -= 1
else: 
        pass

if uppercase == False: 
    strength -=1
else: 
     pass

