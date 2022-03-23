import time
import turtle
from turtle import Turtle,Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import Scoreboard


Range=-300

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PING PONG")
screen.tracer(0)


for i in range(20):
    timmy = Turtle()
    timmy.penup()
    timmy.shape("square")
    timmy.color("white")
    timmy.turtlesize(stretch_wid=1, stretch_len=0.3)
    a=timmy.goto(0,Range+30)
    Range+=30




r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()





screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down ,"Down")

screen.onkey(l_paddle.w,"w")
screen.onkey(l_paddle.s ,"s")



game_on=True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



    if ball.distance(r_paddle) <50 and  ball.xcor()>330 or ball.distance(l_paddle) <50 and  ball.xcor() <-330:
        ball.bounce_x()



    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.final_score_1()


    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.final_score_2()



screen.exitonclick()



