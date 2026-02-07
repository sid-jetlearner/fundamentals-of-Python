import turtle
import random
screen=turtle.Screen()
screen.bgcolor('blue')
q=turtle.Turtle()
q.shape("square")
q.color('black')
q.penup()
q.goto(0,100)
gameover=False
pen=turtle.Turtle()
q.direction="stop"
def go_up():
    q.direction="up"
def go_down():
    q.direction="down"
def go_right():
    q.direction="right"
def go_left():
    q.direction="left"
def move():
    if q.direction=="up":
        y=q.ycor()
        q.sety(y+20)
    if q.direction=="down":
        y=q.ycor()
        q.sety(y-20)
    if q.direction=="right":
        x=q.xcor()
        q.setx(x+20)
    if q.direction=="left":
        x=q.xcor()
        q.setx(x-20)
def restart():
    global gameover
    gameover=False
    q.penup()
    q.goto(0,100)
    pen.clear()
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.onkey(go_right,"Right")
screen.onkey(go_left,"Left")
screen.onkey(restart,"r")
while True:
    screen.update()
    if not gameover:
        move()
    if q.xcor()>330 or q.xcor()<-330 or q.ycor()>330 or q.ycor()<-330:
        q.direction='stop'
        gameover=True
        pen.hideturtle()
        pen.penup()
        pen.goto(-100,0)
        pen.pendown()
        pen.write("gameover",font=("Arial",80,"bold"))
        pen.penup()
        pen.goto(-30,-50)
        pen.pendown()
        pen.write("press 'r' to restart",font=("Arial",25,"bold"))
screen.mainloop()