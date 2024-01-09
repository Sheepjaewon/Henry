import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_russian_flag():
    turtle.speed(0)
    turtle.bgcolor("#FFFFFF")  # Set background color to white

    # Draw the white rectangle
    turtle.penup()
    turtle.goto(-200, 100)  # Starting position for the first rectangle
    turtle.pendown()
    draw_rectangle("#FFFFFF", 400, 100)

    # Draw the blue rectangle
    turtle.penup()
    turtle.goto(-200, 0)  # Starting position for the second rectangle
    turtle.pendown()
    draw_rectangle("#0055A4", 400, 100)

    # Draw the red rectangle
    turtle.penup()
    turtle.goto(-200, -100)  # Starting position for the third rectangle
    turtle.pendown()
    draw_rectangle("#D52B1E", 400, 100)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the Russian flag
draw_russian_flag()
