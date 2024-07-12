from turtle import *
import colorsys
speed(0)
pensize(2)
bgcolor('black')
h=0.0

for i in range(250):
    col = colorsys.hsv_to_rgb(h,1,1)
    pencolor(col)
    h+=0.005
    circle(5-i, 100)
    lt(80)
    circle(5-i, 100)
    rt(100)
done()