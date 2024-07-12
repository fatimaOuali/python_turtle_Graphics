from turtle import * 
import math

t = Turtle()
t.speed(0)
bgcolor("black")

rad = 90
an = 10

rad1 = 90
an1 = 10

while True:
    x = rad * math.cos(
        math.radians(an)
    )
    y = rad * math.sin(
        math.radians(an)
    )
    x1 = rad1 * math.cos(
        math.radians(an1)
    )
    y1 = rad1 * math.sin(
        math.radians(an1)
    )

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("white")
    t.circle(rad)

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pencolor("white")
    t.circle(rad1)

    an += 1
    an1 -= 1

    update()
