from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
goto(0, 0)
h = 0
def draw(ang, n):
    circle(n+7,60)
    left(ang)
    circle(n+7, 60)
for i in range(90):
    c = cs.hsv_to_rgb(h,1,1)
    h += 1/70
    color(c)
    up()
    draw(90, i)
    draw(180, i)
    down()
    draw(1/2, i-1)
    draw(180, i)
    draw(120, i-1)
done()

