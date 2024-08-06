from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
pensize(3)
goto(0, 0)
h = 1
   
for i in range(320):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    circle(i+7, 60)
    left(51)
    circle(i+7, -60)

done()

