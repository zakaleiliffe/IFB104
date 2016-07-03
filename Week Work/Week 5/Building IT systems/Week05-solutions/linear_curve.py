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

# A function to draw a linear curve
#
def linear_curve():
 
    # Set the length of each line
    limit = 300

    # Set the separation on the axes of each line
    line_sep = 10

    # Lift the pen up
    penup()

    # For each of the points along the axis:
    points = range(0, limit + 1, line_sep)
    for line_num in points:

            # Draw one line of a linear curve quarter
            goto(limit, line_num)
            pendown()
            goto(limit - line_num, limit)
            penup()


##            # Challenge: Draw four curves, to form a circle
##
##            # A helper function to draw one line for the "challenge" code
##            #
##            def draw_line(start_x, start_y, finish_x, finish_y):
##                goto(start_x, start_y)
##                pendown()
##                goto(finish_x, finish_y)
##                penup()
##    
##            # Spread the four corners out so they don't overlap
##            offset = limit - (limit / 4)
##
##            # Top right corner (already done above)
##            # draw_line(limit, line_num, limit - line_num, limit)
##            # Bottom left corner
##            draw_line(0 - offset, limit - line_num - offset,
##                      line_num - offset, 0 - offset)
##            # Bottom right corner            
##            draw_line(line_num, 0 - offset, limit, line_num - offset)
##            # Top left corner            
##            draw_line(0 - offset, line_num, line_num - offset, limit)

    
#---------------------------------------------------------
# Main program to call your linear_curve function
#
title("Linear curve")
speed('fastest')
linear_curve()
hideturtle()
done()
