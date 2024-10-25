from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=5)
        self.color('blue')
        self.goto(position)


    def move_right(self):
        print('yes')
        new_cor = (self.xcor() + 20)
        self.goto(new_cor, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


