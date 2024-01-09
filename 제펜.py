import turtle

def draw_circle(color, radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.hideturtle()

def draw_japanese_flag():
    turtle.speed(0)
    turtle.bgcolor("#FFFFFF")  # Set background color to white

    # Draw the red circle
    draw_circle("#DC143C", 200)

    turtle.done()

# Call the function to draw the national flag of Japan
draw_japanese_flag()
