from turtle import *
import colorsys as cs

tracer(10)
speed(0)
bgcolor('black')
pensize(5)
h = 0

for i in range(272):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.01
    color(c)
    circle(i, 90)
    right(181)
    circle(i, 90)
    right(180)
done()
