from turtle import *
import colorsys as cs

speed(0)
pensize(2)
bgcolor('black')
h = 0.4

for i in range(180):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.006
    color(c)
    lt(50)
    lt(30)
    circle(60)
    fd(14)
    right(91)
done()





