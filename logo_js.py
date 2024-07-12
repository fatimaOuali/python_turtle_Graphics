import turtle

# Create a turtle screen and set background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
tle = turtle.Turtle()

# Set the turtle color to yellow
tle.color("yellow")

# Move the turtle to the starting position
tle.penup()
tle.goto(-50, 50)
tle.pendown()

# Begin filling the shape
tle.begin_fill()

# Draw the square
for _ in range(4):
    tle.forward(150)
    tle.right(90)

# End filling the shape
tle.end_fill()

# Move the turtle to the center of the square
tle.penup()
tle.goto(54, -100)
tle.pendown()

# Write "Ml" in the center of the square
tle.color("black")  # Set the color for the text
tle.write("JS", align="center",
           font=("Arial", 48, "bold"))

# Close the turtle graphics window when clicked
screen.exitonclick()
