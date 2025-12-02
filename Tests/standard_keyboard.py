import msvcrt

print("Press any key, press 'q' to quit.")

while True:
    if msvcrt.kbhit():  # check if a key was pressed
        key = msvcrt.getch()
        
        # Arrow keys and special keys return two bytes
        if key == b'\xe0':  
            key2 = msvcrt.getch()
            if key2 == b'H':
                print("Up arrow")
            elif key2 == b'P':
                print("Down arrow")
            elif key2 == b'K':
                print("Left arrow")
            elif key2 == b'M':
                print("Right arrow")
        else:
            # Normal keys
            char = key.decode('utf-8')
            print("You pressed:", char)
            if char == 'q':
                print("Exiting...")
                break