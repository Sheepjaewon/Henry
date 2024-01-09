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

def draw_german_flag():
    turtle.speed(0)
    turtle.bgcolor("#000000")  # Set background color to black

    # Draw the black rectangle
    turtle.penup()
    turtle.goto(-200, 100)  # Starting position for the first rectangle
    turtle.pendown()
    draw_rectangle("#000000", 400, 100)

    # Draw the red rectangle
    turtle.penup()
    turtle.goto(-200, 0)  # Starting position for the second rectangle
    turtle.pendown()
    draw_rectangle("#FF0000", 400, 100)

    # Draw the gold rectangle
    turtle.penup()
    turtle.goto(-200, -100)  # Starting position for the third rectangle
    turtle.pendown()
    draw_rectangle("#FFCE00", 400, 100)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the German flag
draw_german_flag()
