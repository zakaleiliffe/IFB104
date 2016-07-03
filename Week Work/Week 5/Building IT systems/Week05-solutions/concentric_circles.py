#---------------------------------------------------------
#
#  Concentric Circles
#
#  In an earlier workshop exercise you developed a program
#  which drew three concentric circles.  Here we will
#  illustrate the power of repetitive code by developing
#  functions that draw as many circles as we want.
#
#  In this exercise you will define three Turtle graphics
#  functions, "draw_circles_for", "draw_circles_while"
#  and "draw_circles_recursive", each of which draws a set of
#  concentric circles centred on the screen's origin.  Each
#  function must accept three parameters, the minimum circle
#  radius, the maximum circle radius, and the separation
#  between the radii of successive circles.
#
#  This behaviour can be implemented easily using a FOR loop,
#  and with only a little more thought using a WHILE loop or
#  recursively.  Try doing it in all three ways.
#

from turtle import *


#---------------------------------------------------------

## DEVELOP YOUR THREE FUNCTIONS HERE

# A version using a FOR loop
def draw_circles_for(min_radius, max_radius, step_size):
    radii = range(min_radius, max_radius, step_size)
    for radius in radii:
        penup()
        goto(radius, 0) # easternmost point
        setheading(90) # point north
        pendown()
        circle(radius) # walk in a circle

# A version using a WHILE loop
def draw_circles_while(min_radius, max_radius, step_size):
    radius = min_radius
    while radius <= max_radius:
        penup()
        goto(radius, 0) # easternmost point
        setheading(90) # point north
        pendown()
        circle(radius) # walk in a circle
        radius += step_size

# A recursive version
def draw_circles_recursive(radius, max_radius, step_size):
    if radius <= max_radius:
        penup()
        goto(radius, 0) # easternmost point
        setheading(90) # point north
        pendown()
        circle(radius) # walk in a circle
        draw_circles_recursive(radius + step_size,
                               max_radius, step_size)


#---------------------------------------------------------
#
# This main program calls one of your functions.  Uncomment
# the appropriate call for the function you are developing.
#

# Set up
title("Concentric circles")
speed("fastest")

# Test the functions by drawing circles ranging from 5 to
# 250 pixels in radius, in steps of 10 pixels.
# Uncomment these calls one at a time to test your functions.
#
draw_circles_for(5, 250, 10)
# draw_circles_while(5, 250, 10)
# draw_circles_recursive(5, 250, 10)

# Clean up
hideturtle()
done()


