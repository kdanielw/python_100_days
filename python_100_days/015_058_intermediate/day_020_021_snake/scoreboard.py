from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x = 0, y = 270)
        self.hideturtle()        

        self.score = -1
        self.high_score = 0
        self.inscrease_score()
    
    def inscrease_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = -1
        self.inscrease_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)