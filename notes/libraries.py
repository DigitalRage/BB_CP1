#BB 1st Libraries and built in functions
import turtle as t
import random

def draw_branch(branch_length):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15)
        t.left(40)
        draw_branch(branch_length - 15)
        t.right(20)
        t.backward(branch_length)

t.speed('fastest')
t.left(90)
t.up()
t.backward(100)
t.down()
draw_branch(100)
t.done()

draw_branch(10)

"""colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
side = random.randint(10, 500)

screen = t.Screen()
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

t.colormode(255)
t.pencolor((0, 0, 0))
t.width(500)
screen.tracer(0)
for i in range(1, 10000):
    t.forward(1+i)
    t.right(300)
    t.forward(20)
    t.pencolor(((i * 1) % 255, (i*100) % 255, (i * 1000) %255))
screen.tracer(1)
t.done()
"""
