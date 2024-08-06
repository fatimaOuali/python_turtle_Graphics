from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(3)


for i in range(520):
    c = cs.hsv_to_rgb(i/6,1,1)
    color(c)
    forward(i)
    right(90)

done()









