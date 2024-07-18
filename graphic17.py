from turtle import *
import colorsys as cs

tracer(10)
speed(0)
bgcolor('black')
pensize(3)
h = 0.5

for i in range(132):
    for j in range(8):
        c = cs.hsv_to_rgb(h,i/132,j/8)
        color(c)
        goto(0,0)
        circle(i, 90)
        forward(120)
        right(180)
    left(45)
done()
