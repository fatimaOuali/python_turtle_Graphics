from turtle import *
import colorsys as cs

tracer(10)
bgcolor('black')
pensize(5)
h = 0

for i in range(120):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.01
    color(c)
    goto(0,0)
    circle(i, 90)
    forward(60)
    right(180)
done()  

