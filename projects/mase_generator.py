# add libraries
import turtle as t
import random as r

#size of line
s = 50
#sets up screen module
screen = t.Screen()
#list of all made lines
spaces = [[-500,-500,500,0], [-500,0,0,0], [0,0,0,450], [0,-450,450,450]]
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

for i in range(1,5000):
    
    x = r.randint(1,10)
    y= r.randint(1,10)

    #checks what angle the line is, so that it can go that way
    rotation = r.randint(1,4)
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
    def cordinate_finder(var): 
        var = var * 50
        return var

    angle = rotation * 90

    x = cordinate_finder(x)
    x2 = cordinate_finder(x2)
    y = cordinate_finder(y)
    y2 = cordinate_finder(y2)

    #x cordinate
    #y cordanite
    spaces.append([x,x2,y,y2])

    
for list in spaces: 
    x = list[1]
    x2 = list[2]
    y = list[3]
    y2 = list[4]
    t.goto(x,y)
    t.pendown()
    t.goto(x2,y2)
    t.penup()
t.done()