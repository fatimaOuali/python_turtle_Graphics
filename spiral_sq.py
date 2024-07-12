import turtle

def draw(side_length, num_squares,angle):
    for _ in range(num_squares):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        turtle.left(angle)
        side_length += 1

turtle.speed(0)

draw(1, 300, 5)

turtle.exitonclick()
