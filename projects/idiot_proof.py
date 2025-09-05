# BB 1st Idiot Proof Project
full_name = input("What is your full name: ").strip().lower().title()
while True: 
    p_number = input("What is your phone number? GIVE IT TO ME: ")
    if p_number.isdigit():
        p_num1 = p_number[0:3]
        p_num2 = p_number[3:6]
        p_num3 = p_number[6:10]
        break
    else:
        print("Invalid phone number. Make sure it's exactly 10 digits, no spaces or symbols.") 

while True:
    gpa = input("What is your GPA: ")
    if gpa.replace(".","",1).isdigit(): 
        gpa_float = float(gpa)
        break
    else: 
        print("That is not a valid GPA. Please try again. ")

print(f"\nThis is your identity: \nname: {full_name} \nphone: {p_num1, p_num2, p_num3} \nGPA: {gpa_float:.1f}")