from turtle import *
import random

speed(0)
bgcolor("black")
pensize(1)

clr = [
    "skyblue", "Hotpink", 
     "orange", "lime",
    "yellow", "purple",
     "red", "cyan" 
]

p = Pen()

for i in range(400):
    p.pencolor(random.choice(clr))
    p.width(i / 100 + 2)
    p.forward(i)
    p.left(100)

done()
