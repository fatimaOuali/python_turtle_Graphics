import turtle
import random

# تحديد قائمة لتخزين مراكز المرسومات
centers = []

def draw(radius, num, color, x, y):
    angle = 360 / num
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    for _ in range(num):
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.left(angle)

# تحديد سرعة الرسم
turtle.speed(0)
turtle.bgcolor("black")

# تحديد قائمة لتخزين الألوان المستخدمة
used_colors = []

# رسم سبع دوائر بأحجام وأماكن وألوان عشوائية وغير متكررة
for _ in range(7):
    while True:
        rc = random.choice(
            [
                "red", "purple", 
                "yellow", "green",
                  "blue", "Hotpink",
                    "gray"])
        if rc not in used_colors:
            used_colors.append(rc)
            break

    rds = random.randint(50, 100)

    # توليد موقع عشوائي يتجنب التداخل
    while True:
        rx = random.randint(-300, 300)
        ry = random.randint(-300, 300)
        if all(
            (
                (x - rx)**2 + (y - ry)**2)
                  >= (rds + radius)**2
            for (x, y, radius) in centers
        ):
            break

    # رسم الدائرة وتخزين مركزها
    draw(rds, 60, rc, rx, ry)
    centers.append((rx, ry, rds))

# إنهاء البرنامج بعد الانتهاء من الرسم
turtle.done()
