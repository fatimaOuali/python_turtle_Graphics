from turtle import *
import colorsys as cs

bgcolor("black")
speed(0)
h = 0.7

for i in range(100):
    c = cs.hsv_to_rgb(h, 1, 1)
    h += 0.001
    goto(0, 0)
    color(c)
    circle(i, 90)
    circle(100)
left(10)
done()
