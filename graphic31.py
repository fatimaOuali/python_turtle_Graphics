from turtle import *
import colorsys as cs

speed(0)
pensize(2)
bgcolor('black')
h = 0.4

for i in range(140):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.006
    color(c)
    goto(0, 0)
    lt(90)
    lt(40)
    forward(190)
    lt(50)
    fd(20)
    right(46)
done()






