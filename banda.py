from turtle import *

t = Turtle()
Screen().bgcolor("skyblue")

def banda(color, r):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t.up()
t.setpos(-35, 95)
t.down()
banda('black',20)

t.up()
t.setpos(35, 95)
t.down()
banda('black',20)

t.up()
t.setpos(0, 35)
t.down()
banda('white',45)

t.up()
t.setpos(-18, 75)
t.down()
banda('black', 13)

t.up()
t.setpos(18, 75)
t.down()
banda('black',13)

t.up()
t.setpos(-18, 77)
t.down()
banda('white',9)

t.up()
t.setpos(18, 77)
t.down()
banda('white',9)

t.up()
t.setpos(0, 55)
t.down()
banda('black', 10)

t.up()
t.setpos(0, 55)
t.down()
t.right(90)
t.circle(10, 180)


t.up()
t.setpos(0, 55)
t.down()
t.left(360)
t.circle(10, -180)
t.hideturtle()

done()