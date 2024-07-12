from turtle import *
import colorsys as cs
tracer(3)
pensize(6)
bgcolor('black')
h = 0
for i in range(270):
    c = cs.hsv_to_rgb(h,i/270,1)
    color(c)
    lt(97)
    circle(i*2, steps=2)
    rt(10)    
done()