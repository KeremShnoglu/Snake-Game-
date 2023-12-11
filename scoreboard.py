from turtle import Turtle
FONT=("arrial",16,"normal")
ALİNGMENT="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score= {self.score} ",False,align=ALİNGMENT,font=FONT)
        self.hideturtle()
    def get_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score= {self.score} ",False,align="center",font=("arrial",20,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f" GAME OVER ", False, align="center", font=("arrial", 16, "normal"))