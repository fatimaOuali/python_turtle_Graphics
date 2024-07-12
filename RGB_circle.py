from turtle import *
import colorsys
colormode(255)
bgcolor('black')
tracer(3) 
pensize(4)
h = 0.1
for i in range(360):
    hue = h / 360
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    pencolor(r, g, b)
    h += 1
    goto(0, 0)
    left(1)
    fd(120)
done()