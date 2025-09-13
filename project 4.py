import turtle
D=turtle.Turtle()
#circle-sun
D.color("yellow")
D.up()
D.goto(100,100)
D.down()
D.begin_fill()
for i in range (60):
    D.forward(6)
    D.left(6)
D.end_fill()
#rect-sand
D.color("gold")
D.up()
D.goto(-800,-100)
D.down()
D.begin_fill()
for i in range (2):
    D.forward(1600)
    D.right(90)
    D.forward(600)
    D.right(90)
D.end_fill()
#triangle-pyramid
D.color("goldenrod")
D.up()
D.goto(-300,-100)
D.down()
D.begin_fill()
for i in range (3):
    D.forward(200)
    D.left(120)
D.end_fill()
turtle.done()
