from turtle import * 
import colorsys

speed(0)
pensize(1)
bgcolor("black")
fl = 0.6

for i in range(180):
    col = colorsys.hsv_to_rgb(
        fl,1,1
    )
    fl += 0.004
    fillcolor(col)
    begin_fill()
    circle(150 - i, 90)
    lt(90)
    circle(150 - i, 90)
    lt(10)
    end_fill()
done()