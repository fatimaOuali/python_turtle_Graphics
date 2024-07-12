from turtle import *
import colorsys

speed(0)
pensize(1)
bgcolor("black")
f = 1   

for i in range(150):
    col = colorsys.hsv_to_rgb(
        f,1,1
    )
    f += 0.004
    fillcolor(col)
    begin_fill()
    circle(150 - i, 80)
    lt(90)
    circle(150 - i,80)
    lt(10)
    end_fill()

done()

