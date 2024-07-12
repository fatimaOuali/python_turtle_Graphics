from turtle import *
import colorsys

t = Turtle()
s = Screen()
s.bgcolor("black")
t.speed(0)

n =37
h = 0

for i in range(480):
    c = colorsys.hsv_to_rgb(
        h, 1, 1
        )
    h += 1/n
    t.color(c)
    t.left(30)
    for j in range(5):
        t.forward(70)
        t.left(10)
