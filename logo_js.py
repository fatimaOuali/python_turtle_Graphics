from turtle import *
 
bgcolor('black')
color('yellow')
up()
goto(-50, 50)
down()
begin_fill()
for _ in range(4):
    forward(150)
    right(90)
end_fill()
up()
goto(54, -100)
down()
color('black')
write("JS", align="center",
      font=("Arial", 48, "bold"))
done()
