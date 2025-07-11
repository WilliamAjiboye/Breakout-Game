import random
from turtle import Turtle


random_x = random.randint(-380, 380)
random_y = -40

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = .1
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(random_x,random_y)
        self.x_move = 10
        self.y_move = 10
        # self.speed(1)

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()-self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    def reset(self):
        self.goto(random_x,random_y)




