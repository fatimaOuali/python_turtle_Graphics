from turtle import *
import colorsys as cs
tracer(50)
pensize(3)
bgcolor('black')
h = 1
    
for i in range(438):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    goto(0, 0)
    circle(160 - i / 4, 90)
    right(180)
    forward(100)
    
done()

