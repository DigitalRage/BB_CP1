from turtle import*

def draw_branch(): 
    if length > 5:
        for i in range(3): 
            t.forward()
            draw_branch(length)
            t.right(60)


t = Turtle()
t.speed(0)
t.color("light blue")
t.penup()
t.goto(0,0)
