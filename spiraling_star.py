from turtle import *

t = Turtle()
t.speed(10)
bgcolor("black")

len = 4

for i in range(300):
    t.pencolor("red")
    t.forward(len)
    t.right(200)
    len = len - 4

t.hideturtle()
done()
