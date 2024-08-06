from turtle import *
import colorsys as cs

speed(0)
pensize(3)
bgcolor('black')
h = 0
for i in range(140):
    c = cs.hsv_to_rgb(h,1,1)
    h += 1/80
    color(c)
    goto(0, 0)
    circle(160 - i / 4, 90)
    circle(50)
    circle(160 - i / 4, -60)
    right(90)
done()
