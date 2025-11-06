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
    
    x1 = r.randint(1,9)
    y1 = r.randint(1,9)

    #checks what angle the line is, so that it can go that way
    rotation = r.randint(1,4)
    angle = rotation * 90
    if rotation == 1: 
        x2 = x1
        y2 = y1 - 1
    elif rotation == 2: 
        x2 = x1 - 1
        y2 = y1
    elif rotation == 3: 
        x2 = x1
        y2 = y1 + 1
    elif rotation == 4: 
        x2 = x1 + 1
        y2 = y1
    #Finds the cordinates in the x and y values
    def cord(var): 
        var = var * 50
        return var


    x1 = cord(x1)-500
    x2 = cord(x2)-500
    y1 = cord(y1)
    y2 = cord(y2)

    #x cordinate
    #y cordinite
    cords.append([x1,x2,y1,y2,angle])

def filtered_cords(data): 
    filtered_list = []
    seen_points = set()

    for item in data: 
        x1, x2, y1, y2, *rest = item

        point1 = (x1,y1)
        point2 = (x2,y2)


    if point1 not in seen_points or point2 not in seen_points: 
        filtered_list.append(item)
        seen_points.add(point1)
        seen_points.add(point2)

    return filtered_list

coords = filtered_cords(cords)

#pulls angle & cordnate
for list in coords: 
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