# add libraries
import turtle as t
import time as T
import random as r

#size of line
s = 50
#sets up screen module
screen = t.Screen()
screen.tracer(0)
#list of all made lines
#sets to fastest speed
t.speed(0)
#lifts pen
t.penup()

while True:
    
    cords = [[-500,-500,500,0], [-500,-50,0,0], [0,0,0,500], [0,-450,500,500]]
    for i in range(1,5000):

        x1 = r.randint(1,9)
        y1 = r.randint(1,9)

        #checks what angle the line is, so that it can go that way
        rotation = r.randint(1,4)
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
        cords.append([x1,x2,y1,y2])

    def filtered_cords(data): 
        #where non cordinate duplictes go.  
        filtered_list = []
        seen_points = set()

        for item in data: 
            x1, x2, y1, y2 = item
            point1 = (x1, y1)
            point2 = (x2, y2)

            if point1 not in seen_points or point2 not in seen_points: 
                filtered_list.append(item)
                seen_points.add(point1)
                seen_points.add(point2)

        return filtered_list

    coords = filtered_cords(cords)

    #coordinates to the enterances
    item_remove1 = [-500,-450,450,450]
    item_remove2 = [-450,-500,450,450]
    item_remove3 = [0,-50,50,50]
    item_remove4 = [-50,0,50,50]
    items_remove = (item_remove1, item_remove2, item_remove3, item_remove4)

    #removes permanate softlock by opening enterances
    while item_remove1 in coords: 
        coords.remove(item_remove1)
    while item_remove2 in coords: 
        coords.remove(item_remove2)
    while item_remove3 in coords: 
        coords.remove(item_remove3)
    while item_remove4 in coords: 
        coords.remove(item_remove4)

    #main loop that places lines
    for list in coords: 
        #pulls x & y
        x1 = list[0]
        x2 = list[1]
        y1 = list[2]
        y2 = list[3]
        t.penup()
        t.goto(x1,y1)
        t.pendown()
        t.goto(x2,y2)

    screen.tracer(1)
    T.sleep(1)
    screen.tracer(0)

    for i in range(1, 5000): 
        t.undo()
screen.tracer(1)



t.done()

"""def check_collision_with_boundaries(point_x, point_y, boundaries):
    """
    Checks if a given point (point_x, point_y) is inside any of the 
    defined rectangular boundaries.
    """
    for box in boundaries:
        # Assuming the order is [x1, x2, y1, y2]
        # We need to determine the min/max of x and y because the order isn't guaranteed
        x_min = min(box[0], box[1])
        x_max = max(box[0], box[1])
        y_min = min(box[2], box[3])
        y_max = max(box[2], box[3])

        # The core collision logic using chained comparisons
        if x_min <= point_x <= x_max and y_min <= point_y <= y_max:
            # Collision detected within this specific box
            return True 
            
    # If the loop finishes without finding any collision
    return False

# --- Example Usage ---

# Test a point that is likely inside one of the examples (e.g., in the fourth box)
test_point_1_x, test_point_1_y = -200, 500
if check_collision_with_boundaries(test_point_1_x, test_point_1_y, coord_list):
    print(f"Point ({test_point_1_x}, {test_point_1_y}) is colliding.")
else:
    print(f"Point ({test_point_1_x}, {test_point_1_y}) is not colliding.")

# Test a point that is likely outside
test_point_2_x, test_point_2_y = 100, 100
if check_collision_with_boundaries(test_point_2_x, test_point_2_y, coord_list):
    print(f"Point ({test_point_2_x}, {test_point_2_y}) is colliding.")
else:
    print(f"Point ({test_point_2_x}, {test_point_2_y}) is not colliding.")"""