import turtle

def draw_french_flag():
    screen = turtle.Screen()
    screen.setup(600, 400)  # Set the size of the drawing window
    screen.bgcolor("white")

    my_turtle = turtle.Turtle()
    my_turtle.speed(2)  # Set the drawing speed

    # Draw the blue stripe
    my_turtle.penup()
    my_turtle.goto(-200, 150)
    my_turtle.pendown()
    my_turtle.color("#0055A4")
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(400)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.end_fill()

    # Draw the white stripe
    my_turtle.penup()
    my_turtle.goto(-200, 50)
    my_turtle.pendown()
    my_turtle.color("white")
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(400)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.end_fill()

    # Draw the red stripe
    my_turtle.penup()
    my_turtle.goto(-200, -50)
    my_turtle.pendown()
    my_turtle.color("#EF4135")
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(400)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.end_fill()

    # Hide the turtle and keep the window open
    my_turtle.hideturtle()
    turtle.done()

# Call the function to draw the French flag
draw_french_flag()
port
