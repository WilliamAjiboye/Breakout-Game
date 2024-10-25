from turtle import Turtle


class Bricks:
    def __init__(self):
        self.bricks_list = []
        self.rows = 8 # Number of color rows
        self.columns = 10  # Bricks per row
        self.start_x = 360
        self.start_y = -40
        self.colors = ['yellow', 'yellow', 'green', 'green', 'orange', 'orange', 'red', 'red']

    def create_bricks(self):
        for row in range(self.rows):
            for col in range(self.columns):
                # Initialize turtle for each brick
                brick = Turtle('square')
                brick.shapesize(stretch_len=3.9)
                brick.penup()
                brick.color(self.colors[row])

                # Calculate and set position
                x_pos = self.start_x - (col * 80)
                y_pos = self.start_y + (row * 22)
                brick.goto(x_pos, y_pos)

                # Append brick to list
                self.bricks_list.append(brick)

