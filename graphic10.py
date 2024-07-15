from turtle import *
import colorsys

tracer(10)
bgcolor("black")
pensize(4)
h = 0.1

for i in range( 200):
    c=colorsys.hsv_to_rgb(h,1,1)
    h += 1/90
    pencolor(c)
    circle(i*0.1,90)
    forward(i)
    right(270)
    circle(i, 270)
    forward(i)
    right(180)     
done()
