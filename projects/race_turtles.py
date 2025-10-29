# BB 1st Turtle Race Project

import turtle as t
import random
colors = ["red", "blue", "green", "yellow"]

screen = t.Screen()
t.shape("turtle")

t.penup()
t.fillcolor("black")
screen.tracer(0)
for i in range(1, 4):
    
    t.goto(-200 + (i*50) , 500)

screen.tracer(1)


t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle() 
t4 = t.Turtle()


while True:
    t1.forward(random.randint(5,10))
    t2.forward(random.randint(5,10))
    t3.forward(random.randint(5,10))
    t4.forward(random.randint(5,10))
    
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