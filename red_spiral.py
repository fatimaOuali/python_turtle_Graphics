from turtle import *

speed(0)

p = Pen()
bgcolor("black")

for i in range(400):
    p.pencolor("red")
    p.width(i / 100 + 2)
    p.forward(i)
    p.left(70)

done()