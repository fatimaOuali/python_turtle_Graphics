from turtle import *
bgcolor('skyblue')
def draw_shape():
    color('black', 'orange')
    penup()
    goto(-100, -150)
    begin_fill()
    pendown()
    forward(200)
    left(60)
    forward(80)
    setheading(180)
    forward(280)
    left(120)
    forward(80)
    end_fill()
    backward(80)
    setheading(0)
    forward(140)
    left(90)
def draw_mast_and_sails():
    pensize(8)
    forward(125)
    backward(5)
    penup()
    left(130)
    pensize(2)
    pendown()
    forward(4)
    color('white')
    begin_fill()
    forward(165)
    setheading(0)
    forward(125)
    end_fill()
    penup()
    left(90)
    forward(108)
    right(90)
    forward(7)
    right(40)
    pendown()
    begin_fill()
    forward(168)
    setheading(180)
    forward(125)
    end_fill()
    penup()
draw_shape()
draw_mast_and_sails()
done()