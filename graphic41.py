from turtle import *
import colorsys as cs

speed(0)
pensize(2)
bgcolor('black')
h = 0
for i in range(70):
    c = cs.hsv_to_rgb(h,1,1)
    h+= 0.004
    color(c)
    goto(0, 0)
    for j in range(4):
        forward(i)
        right(50)
        left(10)
        circle(70 - i, 50)
    right(120)
done()






