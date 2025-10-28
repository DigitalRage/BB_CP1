#BB 1st Libraries and built in functions
import turtle as t
import random
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
side = random.randint(10, 500)



t.speed(0)


t.color(random.choice(colors))
t.shape("turtle")

t.width(50)
t.fillcolor(random.choice(colors))
t.begin_fill()
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.end_fill()

t.penup()
t.goto(50, 50)

t.pendown()
t.fillcolor(random.choice(colors))
t.begin_fill()
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.end_fill()

for i in range(1, 1000):
    t.forward(1+i)
    t.right(119)
    t.forward(20)
    t.color(random.choice(colors))

t.done()

