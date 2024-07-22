from turtle import * 
import colorsys as cs

speed(0)
pensize(2)
bgcolor("black")
h = 0
for i in range(140):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    goto(0, 0)
    circle(180 - i, 90)
    circle(9)
    forward(14)
    right(45)
done()