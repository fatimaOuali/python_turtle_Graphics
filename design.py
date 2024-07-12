from turtle import *
import colorsys

speed(0)
pensize(1)
bgcolor("black")
hue = 2

for i in range(190):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    hue += 0.005
    pencolor(col)
    begin_fill()
    circle(190 - i , 60)
    lt(60)
    lt(160)
    circle(190 - i , 60)
    rt(100)
    end_fill()
done()
