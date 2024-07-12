from turtle import *

speed(0)

clr = [
    "Hotpink","yellow",
    "skyblue","purple",
    "white","red"
]

p = Pen()
bgcolor("black")
for i in range(400):
    p.pencolor(clr[i % 6])
    p.width(i / 100+2)
    p.forward(i)
    p.left(60)

done()

