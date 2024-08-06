from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(2)
h = 0

for i in range(98):
    c = cs.hsv_to_rgb(h,i/100,1)
    color(c)
    forward(i)
    left(300)
    circle(i - 2)
done()







