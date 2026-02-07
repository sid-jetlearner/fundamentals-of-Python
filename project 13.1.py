import turtle
import random
d=turtle.Turtle()
screen=turtle.Screen()
d.color('maroon')
d.shape('turtle')
d.speed(100)
def clicktomove(x,y):
    x=random.randint(0,310)
    y=random.randint(0,310)
    d.up()
    d.goto(x,y)
    d.down()
screen.listen()
screen.onclick(clicktomove)
screen.mainloop()