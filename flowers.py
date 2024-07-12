from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0.10

for i in range(180):
    col = colorsys.hsv_to_rgb(
        h, 1, 1
    )
    h += 0.005
    fillcolor(col)
    begin_fill()
    circle(160 - i , 90)
    lt(100)
    circle(160 - i ,90)
    lt(10)
    end_fill()

done()
