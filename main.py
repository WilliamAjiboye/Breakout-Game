from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from bricks import Bricks
from scoreboard import Scoreboard

window = Screen()
window.tracer(0)
window.title('Breakout Game')
window.bgcolor('black')
window.setup(width=800,height=800)
window.listen()

paddle = Paddle((0,-350))
ball = Ball()
bricks = Bricks()
score = Scoreboard()

bricks.create_bricks()
window.onkey(paddle.move_right,'Right')
window.onkey(paddle.move_left,'Left')

# Initialize total hits counter
hits = 0
game_is_on = True

while game_is_on:
    if score.lives > 0:
        # Increase speed after 4 and 12 total hits
        if hits >= 4:
            ball.move_speed = max(0.05, ball.move_speed - 0.01)
        elif hits >= 12:
            ball.move_speed = max(0.05, ball.move_speed - 0.01)

        # Add a slight delay based on current ball speed
        sleep(ball.move_speed)
        window.update()
        ball.move()

        # Bounce conditions for walls, paddle, etc.
        if ball.distance(paddle) < 45 and ball.ycor() < -320:
            ball.bounce_y()
        elif ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
        elif ball.ycor() > 380:
            ball.bounce_y()
        elif ball.ycor() < -380:
            score.lose_life()
            ball.reset()

        # Check for collision with each brick in the list
        for items in bricks.bricks_list[:]:
            if ball.distance(items) <= 40:
                # Get brick color
                fill_color, outline_color = items.color()

                # Update score based on brick color
                score.update_score(fill_color)

                # Increase speed for specific brick colors
                if fill_color == 'orange':
                    ball.move_speed = max(0.035, ball.move_speed - 0.01)
                elif fill_color == 'red':
                    ball.move_speed = max(0.035, ball.move_speed - 0.01)

                # Bounce the ball and hide the brick
                ball.bounce_y()
                items.hideturtle()
                hits += 1  # Increment total hits counter

        # Remove invisible bricks from the list to optimize performance
        bricks.bricks_list = [brick for brick in bricks.bricks_list if brick.isvisible()]

    else:
        game_is_on = False
        score.game_over()

window.mainloop()