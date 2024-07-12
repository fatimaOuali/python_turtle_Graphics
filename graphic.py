from turtle import *
import colorsys as cs
tracer(300)
pensize(3)
bgcolor('black')
h = 0 
up()
goto(0,0)
down()
for i in range(70):
        c = cs.hsv_to_rgb(h,1,1)
        h += 0.04
        color(c)
        fd(10)
        circle(i, 4.5)
        for j in range(600):
            lt(971)
            circle(i *0.1, j, steps=2)
            circle(i, 2)
done()