from turtle import *
import colorsys as cs

tracer(10)
bgcolor('black')
pensize(3)
h = 0.9

for i in range(140):
    c = cs.hsv_to_rgb(h,i/140,1)
    color(c)
    goto(0, 0)
    circle(i, 90)
    forward(60)
    right(10)
done()  