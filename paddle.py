from  turtle import  Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 100
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 100
        x = self.xcor()

        self.goto(x, new_y)

    def w(self):
        new_y = self.ycor() + 100
        x = self.xcor()
        self.goto(x, new_y)

    def s(self):
        new_y = self.ycor() - 100
        x = self.xcor()

        self.goto(x, new_y)









