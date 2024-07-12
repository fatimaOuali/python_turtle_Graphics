from turtle import *

def got(x,y):
    penup()
    goto(x,y)
    pendown()
got(-130, -50)
seth(-130)

fillcolor('#F40096')
begin_fill()
circle(130, 90)
circle(40, 80)
circle(200, 50)
end_fill()

got(140, -50)
seth(-50)
fillcolor('#5CE1E6')
begin_fill()
circle(-130, 90)
circle(-40, 80)
circle(-200, 50)
end_fill()

got(0, -70)
fillcolor('#5CE1E6')
seth(-20)
begin_fill()
circle(220, 45)
circle(50, 60)
circle(-120, 40)
circle(50, 160)
circle(250, 60)
end_fill()

got(10, -75)
fillcolor('#F40096')
seth(-160)
begin_fill()
circle(-220, 45)
circle(-50, 60)
circle(120, 40)
circle(-50, 160)
circle(-250, 60)
end_fill()

fillcolor('black')
got(-20, -80)
seth(-120)
begin_fill()
circle(90, 70)
circle(-70, 40)
seth(90)
circle(-70, 40)
circle(90, 70)
end_fill()

fillcolor('black')
got(-13, -90)
seth(-27)
begin_fill()
circle(40, 60)
circle(30, 120)
circle(40, 60)
circle(30, 120)
end_fill()

got(-10, -30)
seth(-27)
begin_fill()
circle(30, 60)
circle(20, 120)
circle(30, 60)
circle(20, 120)
end_fill()

pencolor('#F40096')
pensize(3)
got(6, 10)
seth(90)
circle(60, 50)
circle(10, 180)
circle(5, 160)
pencolor("#5CE1E6")
got(10, 10)
seth(80)
circle(-60, 55)
circle(-10, 180)
circle(-5, 160)

hideturtle()
done()