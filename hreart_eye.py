import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40, 120)
t.pendown()
t.color("red")
t.begin_fill()
t.left(50)
t.forward(20)
t.circle(10, 190)
t.right(110)
t.circle(10, 190)
t.forward(20)
t.end_fill()

t.penup()
t.goto(40, 120)
t.pendown()
t.color("red")
t.begin_fill()
t.left(70)
t.forward(20)
t.circle(10, 190)
t.right(110)
t.circle(10, 190)
t.forward(20)
t.end_fill()

t.penup()
t.goto(-40, 75)
t.pendown()
t.color("black")
t.begin_fill()
t.right(30)
t.circle(40, 180)

turtle.done()



