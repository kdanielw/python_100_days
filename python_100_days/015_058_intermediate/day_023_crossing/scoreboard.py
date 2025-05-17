from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)
ALIGNMENT = "left"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(POSITION)
        self.level = 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def level_up(self):
        self.level += 1
        self.update()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)        
        return False
