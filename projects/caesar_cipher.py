# BB 1st Caeser Cipher Project
#Declares to user what project does
print("This is a Caeser Ciper Encoder/Decoder. \nWhat do You want to do? ")
#Loop for each decode/encode
def encoder(encoded_message):
    encoded_message = list(encode_message)
    encoded_message = ord(encoded_message)
    encoded_message = encoded_message += 

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
        encode_message = input("Type the message you want to encode: \n")
        encoded_message = encoder
    elif decision == 2: 
