from turtle import Turtle

font = ('Arial', 60, 'normal')
alignment ='center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(350, 330)
        self.score = 0
        self.lives = 5
        self.write(self.score, align=alignment, font=font)

    def update_score(self,colour):
        if colour == 'yellow':
            self.clear()
            self.score+=1
            self.write(self.score, align=alignment, font=font)
        elif colour == 'green':
            self.clear()
            self.score += 3
            self.write(self.score, align=alignment, font=font)
        elif colour == 'orange':
            self.clear()
            self.score += 5
            self.write(self.score, align=alignment, font=font)
        elif colour == 'red':
            self.clear()
            self.score += 7
            self.write(self.score, align=alignment, font=font)

    # def live(self):


    def lose_life(self):
        self.lives-=1

    def game_over(self):
        self.home()
        self.write(f'Game Over \n Your score is :{self.score}', align='center', font=font)
    def reset(self):
        self.lives = 5
        self.score = 0
        self.update_score()
