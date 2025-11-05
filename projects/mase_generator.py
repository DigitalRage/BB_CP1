# add libraries
import turtle as t
import random as r

#size of line
s = 50
#sets up screen module
screen = t.Screen()
screen.tracer(0)
#list of all made lines
cords = [[-500,-500,500,0,90], [-500,0,0,0,360], [0,0,0,450,270], [0,-450,450,450,180]]
#lifts pen
t.speed(0)
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
t.right(180)

for i in range(1,5000):
    
    x = r.randint(1,9)
    y = r.randint(1,9)

    #checks what angle the line is, so that it can go that way
    rotation = r.randint(1,4)
    angle = rotation * 90
    if rotation == 1: 
        x2 = x
        y2 = y - 1
    elif rotation == 2: 
        x2 = x - 1
        y2 = y
    elif rotation == 3: 
        x2 = x
        y2 = y + 1
    elif rotation == 4: 
        x2 = x + 1
        y2 = y
    #Finds the cordinates in the x and y values
    def cord(var): 
        var = var * 50
        return var


    x = cord(x)-500
    x2 = cord(x2)-500
    y = cord(y)
    y2 = cord(y2)

    #x cordinate
    #y cordinite
    cords.append([x,x2,y,y2,angle])

#pulls angle & cordnate
for list in cords: 
    x = list[0]
    x2 = list[1]
    y = list[2]
    y2 = list[3]
    angle = list[4]
    t.penup()
    t.goto(x,y)
    t.right(angle)
    t.pendown()
    t.forward(50)
    t.left(angle)
screen.tracer(1)

t.done()