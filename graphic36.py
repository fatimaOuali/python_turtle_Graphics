from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(2)
h = 0.6

for i in range(200):
    c = cs.hsv_to_rgb(h,i/250,1)
    goto(0, 0)
    color(c)
    forward(i)
    left(300)
    circle(260 - i, 30)
done()







