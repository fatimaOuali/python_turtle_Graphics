from turtle import *
import colorsys

speed(0)
pensize(1)
bgcolor("black")
hue = 0.9

for i in range(220):
    col = colorsys.hsv_to_rgb(
        hue,1,1
    )
    hue += 0.005
    pencolor(col)
    begin_fill()
    circle(300 - i, 50)
    lt(70)
    lt(70)
    circle(300 - i, 50)
    rt(60)
    rt(60)
    end_fill()
done()