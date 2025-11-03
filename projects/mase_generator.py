# add libraries
import turtle as t
import random as r

#size of line
s = 50
#sets up screen module
screen = t.Screen()
#list of all made lines
spaces = [[-500,500,][]]
#lifts pen
t.penup()
t.goto(-500, 500)
t.pendown()
t.right(90)
t.forward(500)
t.left(90)
t.forward(450)
t.penup()
t.forward(50)
t.pendown()
t.left(90)
t.forward(500)
t.left(90)
t.forward(450)
t.pendown()

x = r.randint(1,10)
y= r.randint(1,10)


r.randint(1,10)
rotation = r.randint(1,4)
if rotation == 1: 
    x2 = x
    y2 = y - 1
elif rotation == 2: 
    x2 = x
    y2 = y
elif rotation == 3: 
    x2 = x
    y2 = y + 1
elif rotation == 4: 
    x2 = x
    y2 = y

#x cordinate
#y cordanite
spaces.append([x,y,x2,y2])
t.done()