from turtle import *
import colorsys as cs

tracer(10)
speed(0)
bgcolor('black')
pensize(4)
h = 0
for i in range(110):
    for j in range(8):
        c = cs.hsv_to_rgb(h,i/110,1)
        color(c)
        goto(0,0)
        circle(i, 90)
        forward(150)
        circle(i, -90)
    left(45)
done()
