# BB 1st Caesar Cipher Project
# this shifts a single character and leaves non-letters alone
def shift_char(character, shift):
    #this is for shifting a lowecase letter
    if 'a' <= character <= 'z':
        base = ord('a')
        return chr((ord(character) - base + shift) % 26 + base)
    #this is for shifting an uppercase letter
    if 'A' <= character <= 'Z':
        base = ord('A')
        return chr((ord(character) - base + shift) % 26 + base)
    return character


def encode(text, shift):
    # encode text by shifting each letter forward by shift (shift may be negative)
    result = ''
    for character in text:
        result += shift_char(character, shift)
    return result


def decode(text, shift):
    # decode by shifting backwards
    return encode(text, -shift)


def prompt_int(prompt):
    # simple prompt that allows negative integers
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Please enter a valid integer (e.g. 3 or -2).')


def interactive():
    print('This is a Caesar Cipher Encoder/Decoder.')
    while True:
        print('\n1) Encode')
        print('2) Decode')
        print('3) Quit')
        choice = input('Choose 1/2/3: ').strip()

        if choice == '1':
            text = input('Type the message to encode:\n')
            shift = prompt_int('Shift amount (integer):\n')
            print('\nEncoded:')
            print(encode(text, shift))
        elif choice == '2':
            text = input('Type the message to decode:\n')
            shift = prompt_int('Shift amount used to encode (integer):\n')
            print('\nDecoded:')
            print(decode(text, shift))
        elif choice == '3' or choice.lower() in ('q', 'quit'):
            print('Goodbye!')
            break
        else:
            print('Invalid choice — please enter 1, 2, or 3.')


if __name__ == '__main__':
    interactive()
