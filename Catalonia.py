# Created by: Jess Gallo
# Date Created: 11/10/2023
# Last Modified: 11/10/2023
# Python program that draws the Catalonian flag using turtle

import turtle
import time

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("white")
# set tile of screen
screen.title("Catalonia Flag")
oogway = turtle.Turtle()
# set the cursor/turtle speed. The higher value, faster the is the turtle
oogway.speed(100)
oogway.penup()
# decide the shape of cursor/turtle
oogway.shape("turtle")

# flag height to width ratio is 1:1.9
flag_height = 250
flag_width = 475

# starting points
# start from the first quadrant, half of flag width and half of flag height
start_x = -237
start_y = 125

# For yellow and red stripes (total 9 stripes in flag), each strip width will be flag_height/9
stripe_height = flag_height/9
stripe_width = flag_width


def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()


# This function is used to create 9 yellow and red stripes of the flag
def draw_stripes():
    x = start_x
    y = start_y
    # 4 yellow and 4 red stripes alternatively
    for stripe in range(0,4):
        for color in ["#FCDD09", "#DA121A"]:
            draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
            # decrease value of y by stripe_height
            y = y - stripe_height

    # create last red stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#FCDD09')
    y = y - stripe_height

# start after 5 seconds.
time.sleep(5)
# draw 9 stripes
draw_stripes()
# hide the cursor/turtle
oogway.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()
