from turtle import *

bgcolor('Hotpink')
pencolor('white')
speed(0)
width(23)
penup()
goto(200,-100)
pendown()

left(90)
for i in range(4):
 forward(250)
 circle(80,90)

penup()
goto(85,30)
pendown()
circle(90,360)
penup()
goto(120,150)
pendown()
circle(10,360)

done()