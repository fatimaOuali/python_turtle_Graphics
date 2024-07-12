from turtle import *
import colorsys
s = 4
h = 0.1
speed(0)
hideturtle()
bgcolor("black")
for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.004
    pencolor(c)
    penup()  # ارفع القلم بحيث لا يرسم خطاً
    forward(i * 4/s + 1)
    left(400/s + 0.35)
    pendown()  # أنزل القلم لكي ترسم النقطة
    dot(10)  # ارسم النقطة
    penup()  # ارفع القلم مجدداً للتحرك بدون رسم خط
done()
