from turtle import *
import colorsys as cs

speed(0)
pensize(5)
bgcolor('black')
h = 0.7
for i in range(140):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    goto(0, 0)
    circle(180 - i, 90)
    forward(50)
    circle(180 - i, -60)
    right(90)
done()
