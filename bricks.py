import time
from turtle import Turtle


class Bricks:
    def __init__(self):
        self.bricks = []
        self.start_x = 360
        self.start_y = -100

    def create_bricks(self):
        for i in range(80):

            # elif i == 30:
            #     self.start_x = 360
            #     self.start_y += 22
            # elif i == 50:
            #     self.start_x = 360
            #     self.start_y += 22
            time.sleep(3)
            tim = Turtle('square')
            tim.color('yellow')
            tim.shapesize(stretch_len=3.9)
            tim.penup()
            if i < 20:
                if i == 10:
                    self.start_x = 360
                    self.start_y += 22
                tim.color('yellow')
                tim.goto(self.start_x, self.start_y)
                self.start_x -= 80
                self.bricks.append(tim)
            elif 20 <= i < 40:
                # self.start_y+=22
                tim.color('green')
                tim.goto(self.start_x, self.start_y)
                self.start_x -= 80
                self.bricks.append(tim)
            elif 40 <= i < 60:
                tim.color('orange')
            elif i >= 60:
                tim.color('red')
