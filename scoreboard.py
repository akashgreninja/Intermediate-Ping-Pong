
from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal",)

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score_1=0
        self.score_2=0
        self.penup()
        self.hideturtle()

        self.color("white")
        self.update_scoreboard_1()


    def update_scoreboard_1(self):
        self.clear()
        self.goto(-40,240)

        self.write(f"{self.score_1}", align=ALIGNMENT, font=FONT)
        self.goto(40,240)

        self.write(f"{self.score_2}", align=ALIGNMENT, font=FONT)


    def final_score_1(self):


        self.score_1+=1
        self.update_scoreboard_1()


    def final_score_2(self):

        self.score_2+=1
        self.update_scoreboard_1()


