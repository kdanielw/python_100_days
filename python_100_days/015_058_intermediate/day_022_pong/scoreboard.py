from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
MAX_GOALS = 3

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x = 0, y = 370)
        self.score_p1 = -1
        self.score_p2 = -1
        self.inscrease_score(1)
        self.inscrease_score(2)
    
    def inscrease_score(self, player):
        self.clear()
        if player == 1:
            self.score_p1 += 1
        elif player == 2:
            self.score_p2 += 1
        self.write(f"PLAYER 1  ( {self.score_p1}  X  {self.score_p2} )  PLAYER 2", align=ALIGNMENT, font=FONT)

        if self.score_p1 == MAX_GOALS or self.score_p2 == MAX_GOALS:
            return self.game_over(player)
        return True

    def game_over(self, winner):
        self.goto(x=0, y=50)
        self.write(f"PLAYER {winner} WON!!!", align=ALIGNMENT, font=FONT)
        return False
    