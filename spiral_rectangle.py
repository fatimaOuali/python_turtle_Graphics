from turtle import *
import random

sc = Screen()
sc.bgcolor("black")
sc.title("spiral")

t = Turtle()
t.speed(0)
t.hideturtle()

col = [
    "Hotpink","purple","skyblue"
]

def draw(length, width,curvature, sides):
    for _ in range(sides):
        color = random.choice(col)
        t.pencolor(color)
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90 - curvature)
        length += 2 * curvature
len = 4
wid = 4
cur = 1
sid = 560

t.penup()
t.goto(0, 0)
t.pendown()
draw(len, wid, cur, sid)

t.hideturtle()
done()
