from turtle import *
import colorsys
width(3)
tracer(10)
bgcolor("black")
h = 0.1
n = 20
for i in range( 200):
    c=colorsys.hsv_to_rgb(h,1,1)
    h += 1/n
    pencolor(c)
    circle(i,90)
    forward(i)
    right(270)
    circle(i, 270)
    forward(i)
    right(180)     
done()
