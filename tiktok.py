from turtle import *

width(20)
bgcolor("black")
speed(0)
colors = ["#db0f3c", "#50ebe7", "white"]
pos = [(0, 0), (-5, 13), (-5, 5)]

for (x, y), col in zip(pos, colors):
    up()
    goto(x, y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(120)
    left(180)
    circle(50, 90)


for (x, y),col in zip(pos, colors):
    up()
    goto(x - 110, y - 210)
    down()
    color(col)
    write("TikTok", font=(
        "Arial", 60, "bold"
    ))

done()
