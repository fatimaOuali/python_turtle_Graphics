from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0.5
for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    forward(i * 2/4 + i)
    left(360/4 + 1.5)
    hideturtle()
    color(c)
    pensize(10)
done()



