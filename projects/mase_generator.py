# add libraries
import turtle as t
import random as r
#size of line
screen = t.Screen()
canvas = screen.getcanvas()


    # Example: Check for items overlapping the turtle's current position
    turtle_x, turtle_y = some_turtle.pos()
    # Adjust for tkinter's inverted y-coordinate
    overlapping_items = canvas.find_overlapping(turtle_x, -turtle_y, turtle_x, -turtle_y)

    if overlapping_items:
        first_overlapping_item_id = overlapping_items[0]
        color = canvas.itemcget(first_overlapping_item_id, "fill")
        # Now you can check if 'color' matches your target color
        if color == "red":
            print("Turtle is touching red!")

    # Example: Check if turtle is within a red square at (100, 100) with side 50
    if 100 <= some_turtle.xcor() <= 150 and 100 <= some_turtle.ycor() <= 150:
        print("Turtle is in the red square!")




size = r.randint(1,5)

x = r.randint()
