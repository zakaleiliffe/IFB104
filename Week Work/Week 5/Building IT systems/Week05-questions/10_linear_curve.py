#---------------------------------------------------------
#
# Linear Curve
#
# Define a function called "linear_curve" that uses Turtle
# graphics to draw a linear curve by drawing straight lines
# between increasing/decreasing points on the x axis to
# decreasing/increasing points on the y axis.
#
# See the enclosed file "linear_curve.pdf" for an example
# of the expected output.  Note that you need to write a
# loop that goes through each of the selected points on
# one axis and draws a line to the opposite point on the
# other axis.
#
# Extra challenge:  Extend your function so that it
# draws a "full circle" linear curve.
#

# Import functions required
from turtle import *


#---------------------------------------------------------
#
# Suggested solution strategy for the linear_curve function:
#
# 1. Initialise an integer variable, limit, to represent the line length
#    (notice that each line in the curve is actually of the same length!)
# 2. Lift the pen up
# 3. For every 10th pixel in the line's length (so separate lines can be seen):
#    a. Move the pen to co-ordinates (limit, pixel number)
#    b. Put the pen down
#    c. Draw a line to co-ordinates (limit minus the pixel number, limit)
#    d. Lift the pen up
#

##### DEVELOP YOUR linear_curve FUNCTION HERE

    
#---------------------------------------------------------
# Main program to call your linear_curve function
#
title("Linear curve")
speed('fastest')
# linear_curve()
hideturtle()
done()
