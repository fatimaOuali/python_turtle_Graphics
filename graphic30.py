from turtle import *
import colorsys

speed(0)
pensize(2)
bgcolor('black')
h = 0.4

for i in range(140):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.006
    color(c)
    circle(170 - i, 100)
    lt(90)
    circle(170 - i, 100)
    rt(90)
done()





