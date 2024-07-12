from turtle import *

angle = 91

showturtle()
shape("turtle")
speed(0)
bgcolor("black")

clr = [
    "Hotpink", "yellow", "white"
]

for x in range(200):
    color(clr[x % len(clr)])
    for i in range(4):
        forward(x)
        left(90)
    left(angle)

done()
