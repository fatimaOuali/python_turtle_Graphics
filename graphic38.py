from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(3)
h = 0.6

for i in range(170):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    right(90)
    circle(i*1.1, 90)
    right(59)
done()








