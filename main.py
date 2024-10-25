from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from bricks import Bricks

window = Screen()
window.tracer(0)
window.title('Breakout Game')
window.bgcolor('black')
window.setup(width=800,height=800)
window.listen()

paddle = Paddle((0,-350))
ball = Ball()
bricks = Bricks()
bricks.create_bricks()
window.onkey(paddle.move_right,'Right')
window.onkey(paddle.move_left,'Left')


game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    window.update()
    ball.move()
    if ball.distance(paddle) < 30 and ball.ycor() < -320:
        ball.bounce_y()
    if ball.xcor()>380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.xcor() >=400:
        pass
    for items in bricks.bricks_list[:]:
        if ball.distance(items) <= 30:
            ball.bounce_y()
            items.hideturtle()
    bricks.bricks_list = [brick for brick in bricks.bricks_list if brick.isvisible()]

window.mainloop()