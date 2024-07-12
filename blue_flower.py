from turtle import *
import colorsys

speed(0)
pensize(1)
bgcolor("black")
fl = 0.7

for i in range(180):
    col = colorsys.hsv_to_rgb(
        fl, 1, 1
    )
    fl += 0.005
    fillcolor(col)
    begin_fill()
    circle(150 - i , 90)
    lt(100)
    circle(150 - i ,90)
    lt(10)
    end_fill()

done()
