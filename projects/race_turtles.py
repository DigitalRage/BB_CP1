# BB 1st Turtle Race Project

import turtle as t
import random
colors = ["red", "blue", "green", "yellow"]

screen = t.Screen()

t.penup()
t.fillcolor("black")
screen.tracer(0)
for i in range(1, 4):
    
    t.goto(-200 + (i*50) , 500)

screen.bgcolor("black")

t.speed(0)
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle() 
t4 = t.Turtle()
t5 = t.Turtle()

turtles = [t1, t2, t3, t4, t5]

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t1.color("red")
t2.color("blue")
t3.color("green")
t4.color("yellow")
t5.color("purple")
t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()
t1.goto(-500, 100)
t2.goto(-500, 50)
t3.goto(-500, 0)
t4.goto(-500, -50)
t5.goto(-500, -100)

t.width(3)
t.goto(500, 100)
t.pencolor("white")
t.fillcolor("white")
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
for i in range(2):
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
t.penup()

screen.tracer(1)

while True:
    t1.forward(random.randint(10,15))
    t2.forward(random.randint(10,15))
    t3.forward(random.randint(10,15))
    t4.forward(random.randint(10,15))
    t5.forward(random.randint(10,15))

    
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