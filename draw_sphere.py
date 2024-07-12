from turtle import *
from math import sin, cos, pi
bgcolor("black")
color("white")
speed(0)
pensize(3)
def draw_circle(r, y):
    penup()
    goto(0, r)
    pendown()
    circle(r)
r = 100
n = 36
def draw_sphere():
    for i in range(n):
        angle = i * (pi / n)
        rs = r * sin(angle)
        y = r * cos(angle)
        draw_circle(rs * 2, y)
draw_sphere()
done()