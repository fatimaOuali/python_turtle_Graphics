from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0.2

for i in range(100):
    c = colorsys.hsv_to_rgb(h,1, 1)
    h += 0.01
    pencolor(c)
    lt(200)
    circle(100 - i, 60)
    fd(200)
    circle(100 - i, -80)
done()