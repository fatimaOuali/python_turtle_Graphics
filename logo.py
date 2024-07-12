import turtle
import random

def draw(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(80)

def draw_spiral(nums, init, increment):
    for _ in range(nums):
        # Generate a random color in the format (R, G, B)
        random_color = (
            random.random(),
              random.random(),
                random.random()
                )
        turtle.color(random_color)
        
        draw(init)
        turtle.forward(init)
        turtle.left(80)
        init += increment

def main():
    turtle.speed(0)  # Set the drawing speed (1 to 10, 1 being the slowest, 10 the fastest)
    turtle.hideturtle()  # Hide the turtle icon
    turtle.bgcolor("black")

    nums = 40  # Number of hexagons in the spiral
    init = 4  # Initial side length of the hexagon
    increment = 8  # Increment in side length for each hexagon

    draw_spiral(nums, init, increment)

    turtle.done()  # Finish the drawing

if __name__ == "__main__":
    main()
