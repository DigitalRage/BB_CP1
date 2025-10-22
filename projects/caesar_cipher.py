# BB 1st Caeser Cipher Project
#Declares to user what project does
print("This is a Caeser Ciper Encoder/Decoder. \nWhat do You want to do? ")
#Loop for each decode/encode
def encoder(encoded_message):
    encoded_message = list(encode_message)
    encoded_message = ord(encoded_message)
    encoded_message = encoded_message += number

    return encoded_message
#main loop
while True:
    #person number input for what they want to do
    decision = input("1. Encode\n2. Decode\n3. Quit life\n") 
    #checks if the decision is a digit
    if decision.isdigit(): 
        #makes the number a number if it is a number
        decision = int(decision)
    else: 
        #loops back to start to try again
        print("Try Again")
        continue
    #if you are encoding, encode the message
    if decision == 1: 
        #user encode message
        encode_message = input("Type the message you want to encode: \n")
        #what number they want to encode it to
        number = input("What number do you want to encode to?\n")
        #checks if the number is a number
        if number.isdigit():
            #makes the number a number it is a number
            number = int(number)
        else:
            #makes you redo if it is false
            print("Try Again")
            continue

        encoded_message = encoder
    elif decision == 2: 
