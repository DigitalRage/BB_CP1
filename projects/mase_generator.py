# Import drawing, timing, and random number tools
import turtle as t
import time as T
import random as r

# Set the pixel size of each maze cell
cell_size = 50

# Set up the drawing window
screen = t.Screen()
screen.tracer(0)   # Disable auto-updating for faster drawing
t.speed(0)         # Set turtle to fastest movement
t.penup()          # Start with pen lifted (no lines drawn while moving)

# Convert a maze cell coordinate to a screen pixel coordinate
def to_pixel(cell_x, cell_y):
    pixel_x = cell_x * cell_size - 475
    pixel_y = cell_y * cell_size + 25
    return pixel_x, pixel_y

# Convert pixel position back to nearest maze cell coordinate
def to_cell(px, py):
    cell_x = int(round((px + 475) / cell_size))
    cell_y = int(round((py - 25) / cell_size))
    return cell_x, cell_y

# Loop forever generating random mazes
while True:

    # Create the base maze border walls
    walls = [
        [-500, -500, 500, 0],
        [-500, -50,  0,   0],
        [0,    0,    0,  500],
        [0,   -450, 500, 500],
    ]

    # Randomly add many interior walls
    for _ in range(2000):
        cell_x1 = r.randint(1, 9)
        cell_y1 = r.randint(1, 9)
        direction = r.randint(1, 4)

        if direction == 1:      # Down
            cell_x2 = cell_x1
            cell_y2 = cell_y1 - 1
        elif direction == 2:    # Left
            cell_x2 = cell_x1 - 1
            cell_y2 = cell_y1
        elif direction == 3:    # Up
            cell_x2 = cell_x1
            cell_y2 = cell_y1 + 1
        else:                   # Right
            cell_x2 = cell_x1 + 1
            cell_y2 = cell_y1

        # Convert wall endpoints to pixel coordinates
        walls.append([
            cell_x1 * cell_size - 500,
            cell_x2 * cell_size - 500,
            cell_y1 * cell_size,
            cell_y2 * cell_size
        ])

    # Remove repeated wall segments
    seen_points = set()
    unique_walls = []
    for x_start, x_end, y_start, y_end in walls:
        p1 = (x_start, y_start)
        p2 = (x_end, y_end)
        if p1 not in seen_points or p2 not in seen_points:
            unique_walls.append([x_start, x_end, y_start, y_end])
            seen_points.add(p1)
            seen_points.add(p2)

    # Ensure start and exit openings are never blocked
    openings = [
        [-500, -450, 450, 450],
        [-450, -500, 450, 450],
        [0, -50, 50, 50],
        [-50, 0, 50, 50]
    ]
    for wall in openings:
        while wall in unique_walls:
            unique_walls.remove(wall)

    # Draw all walls on the screen
    for x_start, x_end, y_start, y_end in unique_walls:
        t.penup()
        t.goto(x_start, y_start)
        t.pendown()
        t.goto(x_end, y_end)
    screen.update()

    # Track blocked movements between adjacent cells
    blocked_moves = set()

    # Determine which cell pairs each wall separates
    for x_start, x_end, y_start, y_end in unique_walls:
        mid_x = (x_start + x_end) / 2
        mid_y = (y_start + y_end) / 2

        if x_start == x_end:    # Vertical wall
            sample_points = [(mid_x - 5, mid_y), (mid_x + 5, mid_y)]
        else:                   # Horizontal wall
            sample_points = [(mid_x, mid_y - 5), (mid_x, mid_y + 5)]

        cells = []
        for px, py in sample_points:
            cell_x, cell_y = to_cell(px, py)
            if 0 <= cell_x < 10 and 0 <= cell_y < 10:
                cells.append((cell_x, cell_y))

        if len(cells) == 2:
            c1, c2 = cells
            blocked_moves.add((c1, c2))
            blocked_moves.add((c2, c1))

    # Build graph of valid neighbor movements
    graph = {(x, y): [] for x in range(10) for y in range(10)}

    for x in range(10):
        for y in range(10):
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for nx, ny in neighbors:
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if ((x, y), (nx, ny)) not in blocked_moves:
                        graph[(x, y)].append((nx, ny))

    # Define start and goal cell positions
    start_cell = (0, 9)
    goal_cell = (9, 0)

    # Perform Wave Search (Breadth-First Spread) to find path from start to goal
    frontier = [start_cell]
    came_from = {start_cell: None}

    while frontier:
        current = frontier.pop(0)
        if current == goal_cell:
            break
        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.append(neighbor)

    # If no solution, restart maze creation
    if goal_cell not in came_from:
        t.clear()
        continue

    # Reconstruct found path by backtracking
    path = []
    current = goal_cell
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    # Create turtle to draw the solution path
    solver = t.Turtle()
    solver.shape("turtle")
    solver.color("red")
    solver.speed(0)
    solver.penup()
    solver.goto(*to_pixel(*start_cell))
    solver.pendown()

    # Move step-by-step through path
    for cell_x, cell_y in path:
        solver.goto(*to_pixel(cell_x, cell_y))
        screen.update()
        T.sleep(0.04)

    # Hide solver and remove trace
    solver.hideturtle()
    T.sleep(0.3)
    solver.clear()

    # Clear maze and repeat loop
    T.sleep(0.5)
    t.clear()
