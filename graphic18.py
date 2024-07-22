from turtle import *
import colorsys as cs
bgcolor('black')
speed(0)
h = 0.8
for i in range(300):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.001
    goto(0,0)
    color(c)
    circle(i)
    left(90)
done()
