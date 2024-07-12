from turtle import *
import colorsys

speed(0)
pensize(1)
bgcolor("black")
hue = 2

for i in range(250):
    col = colorsys.hsv_to_rgb(
        hue, 1, 1
    )
    hue += 0.005
    pencolor(col)
    begin_fill()
    circle(240 - i, 60)
    lt(60)
    lt(90)
    circle(240 - i, 60)
    rt(110)
    end_fill()
done()

