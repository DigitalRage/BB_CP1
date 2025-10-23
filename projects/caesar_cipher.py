# BB 1st Caesar Cipher Project
# this shifts a single character and leaves non-letters alone
def shift_char(character, shift):
    #this is for shifting a lowecase letter (%26 to wrap around)
    #ord to get ASCII value of character and chr to convert back to character
    if 'a' <= character <= 'z':
        base = ord('a')
        return chr((ord(character) - base + shift) % 26 + base)
    #this is for shifting an uppercase letter
    if 'A' <= character <= 'Z':
        base = ord('A')
        return chr((ord(character) - base + shift) % 26 + base)
    return character

#encode function that uses shift_char to encode caesar cipher
def encode(text, shift):
    # encode text by shifting each letter forward by shift (shift may be negative)
    result = ''
    for character in text:
        result += shift_char(character, shift)
    return result

#decode function that uses encode to decode caesar cipher
def decode(text, shift):
    # decode by shifting backwards
    return encode(text, -shift)

#function to prompt for number input
def prompt_int(prompt):
    # code that allows negative integers
    while True:
        shift = input(prompt)
        try:
            return int(shift)
        #if not valid integer, reprompt the user
        except ValueError:
            print('Please enter a valid integer (like 3 or -2).')

#descibes the program
print('This is a Caesar Cipher Encoder/Decoder.')
#main loop
while True:
    #options
    print('\n1) Encode\n2) Decode\n3) Quit')
    #user choice input
    choice = input('Choose 1/2/3: ').strip()
    #encode option
    if choice == '1':
        #ask for text and shift amount (applies to decode option as well)
        text = input('Type the message to encode:\n')
        shift = prompt_int('Shift amount (integer):\n')
        #prompts user that the text has been encoded
        print('\nEncoded:')
        #encodes and prints the text
        print(encode(text, shift))
    #decode option
    elif choice == '2':
        text = input('Type the message to decode:\n')
        shift = prompt_int('Shift amount used to encode (integer):\n')
        #prompts user that the text has been decoded
        print('\nDecoded:')
        #decodes and prints the text
        print(decode(text, shift))
    #quit option
    elif choice == '3' or choice.lower() in ('q', 'quit'):
        #prompts user that the program is ending
        print('Goodbye!')
        #ends the program
        break
    #loop back if invalid choice entered
    else:
        #prompts user to try again
        print('Invalid choice — please enter 1, 2, or 3.')
