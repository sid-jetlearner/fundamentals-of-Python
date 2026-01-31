import turtle
import random
player=turtle.Turtle()
screen=turtle.Screen()
player.color("blue")
player.shape("turtle")
player.up()
player.goto(-300,270)
def right():
    player.forward(10)
screen.listen()
screen.onkey(right,"Right")
colors=["red","green","orange","yellow"]
opponents=[]
x=-300
y=170
for clr in colors:
    a=turtle.Turtle()
    a.shape("turtle")
    a.color(clr)
    a.penup()
    a.goto(x,y)
    y-=100
    opponents.append((a,clr))
def moveopponents():
    for a,clr in opponents:
        distance=random.randint(40,80)
        a.forward(distance)
game_over=False
while game_over==False:
    moveopponents()
    for a,clr in opponents:
        if a.xcor()>=200:
            game_over=True
            if a.xcor()<player.xcor():
                winner='Blue'
            else:
                winner=clr
            break
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-200,0)
pen.pendown()
pen.write(f"{winner} wins",font=("Airial",80,"bold"))
screen.mainloop()