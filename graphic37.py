from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')

for i in range(170):
    c = cs.hsv_to_rgb(i/6,i/170,1)
    begin_fill()
    color(c)
    right(90)
    circle(i*1.1, 90)
    end_fill()
    right(59)
done()







