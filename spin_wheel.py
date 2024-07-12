from turtle import *
import colorsys

bgcolor("black")
pensize(3)
pencolor("yellow")
speed(0)
h = 0

goto(0,-140)
circle(140)

# رسم خطوط وسط الدائرة
penup()  # رفع القلم
goto(0, 0)  # الانتقال إلى مركز الدائرة
pendown()  # وضع القلم

for _ in range(12):
    begin_fill()  # بداية التعبئة باللون
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    fillcolor(c)
    left(30)  # دوران القلم بزاوية 30 درجة
    forward(140)  # رسم الخط
    penup()  # رفع القلم
    goto(0, 0)  # الانتقال إلى مركز الدائرة
    pendown()  # وضع القلم
    h += 0.04
    end_fill()  # نهاية التعبئة باللون

done()
