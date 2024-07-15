from turtle import *
import colorsys

tracer(10)
bgcolor("black")
pensize(8)
h = 0

for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.01
    color(c)
    circle(i*0.4, 90)
    forward(i)
    right(271)
    circle(i*0.4, 90)
    forward(i)
    right(180)
done()  