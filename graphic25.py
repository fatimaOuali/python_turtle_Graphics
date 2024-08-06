from turtle import *
import colorsys as cs

speed(0)
pensize(2)
bgcolor('black')
h = 0

for i in range(400):
    c = cs.hsv_to_rgb(h,0.8,1)
    h += 0.006
    color(c)
    circle(i, -90)
    left(54)
    circle(-i, 90)

done()

