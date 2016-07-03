#----------------------------------------------------------------------
#  Luck of the Irish
#
#  As another example of code reuse, in this exercise you will develop
#  a Turtle graphics function to draw a shamrock (a three-leaf clover)
#  and use it to populate an Irish field.
#

# Import the turtle graphics functions
from turtle import *
from random import randint

# Set up the "grassy field"
field_size = 600 # pixels
setup(field_size, field_size)
max_coord = field_size / 2
bgcolor("dark green")
title("Luck of the Irish")

# Adjust the drawing speed, if necessary
speed('fast')


#----------
# Step 1
#
# Define a function that draws a single shamrock.  It should have
# two parameters, the x and y coordinates at which to draw the
# image.  The shamrock should consist of three circular leaves and
# a stem.  Choose an appropriate colour, distinct from the background.

### PUT YOUR FUNCTION DEFINITION HERE




rock_pos_x = randint (-max_coord, max_coord)
rock_pos_y = randint (-max_coord, max_coord)
def shamrock(rock_pos_x, rock_pos_y):
    color = ("green")
    
    goto(rock_pos_x, star_pos_y)
    circle(50)
rock_numbers = range(50)    
for rocks in rock_numbers:
    pendown()
    shamrock(rock_pos_x, rock_pos_y)  

    
    

#----------
# Step 2
#
# Write a main program to display 50 (or so) shamrocks randomly
# positioned on the field.  Use the field size defined above
# to limit the placement of shamrocks.

### PUT YOUR MAIN PROGRAM HERE


# Exit gracefully
hideturtle()
done()
