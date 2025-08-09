import turtle
sid=turtle.Turtle()
sid.speed(100)
sid.color("blue")
sid.begin_fill()
for i in range(8):
    sid.forward(100)
    sid.left(135)
sid.end_fill()
turtle.done()