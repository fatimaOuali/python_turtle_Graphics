from turtle import *
import colorsys

tracer(10)
bgcolor('black')
pensize(5)
h = 0

for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.01
    color(c)
    circle(i, 90)
    right(260)
    circle(i, 90)
    right(180)
done()
