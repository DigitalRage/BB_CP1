# BB 1st Turtle Race Project
# adds turtle library and random library
import turtle as t
import random

#assign screen variable to turtle screen
screen = t.Screen()
#so everything draws instantly
screen.tracer(0)
#set background color to black
screen.bgcolor("black")
#base turtle speed to fastest
t.speed(0)
#all the turtles
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle() 
t4 = t.Turtle()
t5 = t.Turtle()

#make all turtles look like turtles
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
#set different colors for each turtle
t1.color("red")
t2.color("blue")
t3.color("green")
t4.color("yellow")
t5.color("purple")
#lift pens and move turtles to starting position
t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()
#starting positions
t1.goto(-500, 100)
t2.goto(-500, 50)
t3.goto(-500, 0)
t4.goto(-500, -50)
t5.goto(-500, -100)
#sets size of finish line border
t.width(3)
#lift pen to move without drawing
t.penup()
#color of finish line border
t.pencolor("white")
#fill color of finish line
t.fillcolor("white")
#draw finish line squares
for i in range(1, 4):
    t.goto(500, 250 - (i*100))
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.penup()
#draw finish line squares part 2
for i in range(1, 4):
    t.goto(550, 200 - (i*100))
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.penup()
t.goto(550, 150)
t.pendown()
#draw finish line border
for i in range(2):
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
t.penup()
#turtles move normally now
screen.tracer(1)
#main loop for the race
while True:
    #turtle movement
    t1.forward(random.randint(10,15))
    t2.forward(random.randint(10,15))
    t3.forward(random.randint(10,15))
    t4.forward(random.randint(10,15))
    t5.forward(random.randint(10,15))

    #detects cordinates of turtles to see if they crossed finish line
    if t1.xcor() >= 500:
        print("Turtle 1 wins!")
        break
    elif t2.xcor() >= 500:
        print("Turtle 2 wins!")
        break
    elif t3.xcor() >= 500:
        print("Turtle 3 wins!")
        break
    elif t4.xcor() >= 500:
        print("Turtle 4 wins!")
        break