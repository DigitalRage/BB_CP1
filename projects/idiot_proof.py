# BB 1st Idiot Proof Project
full_name = input("What is your full name: ").strip().lower().capitalize()
print(full_name)
p_number = str(float(input("What is your phone number? GIVE IT TO ME: ")))
p_num1 = p_number[0:3]
p_num2 = p_number[3:6]
p_num3 = p_number[6:10]
print(p_num1, p_num2, p_num3)
gpa = float(input("What is your GPA: "))
print(f"GPA: {gpa:.1f}")