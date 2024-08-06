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
    goto(0, 0)
    circle(260 - i, 60 )
    lt(50)
    lt(30)
    right(91)
done()





