# Blaine Buckler 1st Average Grade Project
class_num = 0
grades=[]
range(len(grades))
class_names = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
while class_num < len(class_names):
    grade = float(input(f"What is your {class_names[class_num]} class grade: "))
    grades.append(grade)
    class_num += 1 

average = sum(grades)/len(grades)
print(f"Your current grade average is {average:.2f}")