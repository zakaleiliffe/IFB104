#--------------------------------------------------------------------
#
# Stars and stripes reused
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# stars_and_stripes_flags you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

#some global constants
flag_width = 400
flag_height = 600
stripe_height = 200 #1/3 of total height
star_size = 100
x_offset = 40
y_offset = 10
star_height = 190
star_colour = "black"

# Set up the drawing environment
setup(600, 400)
setworldcoordinates(0, 0,flag_width, flag_height)#sets home
title ('The Ghana Flag')
bgcolor ("white")
penup()
##### PUT YOUR CODE FOR DRAWING THE FLAG HERE
## Draw the bottom green strip
goto(0, stripe_height)
setheading(90)
stripe_numbers = range(1) #Draw first green bottom stripe
for stripe_no in stripe_numbers:
    stripe(flag_width, stripe_height, "dark green")
    forward(stripe_height)

for stripe_no in stripe_numbers:
    stripe(flag_width, stripe_height, "yellow")
    forward(stripe_height)

for stripe_no in stripe_numbers:
    stripe(flag_width, stripe_height, "red")
    forward(stripe_height)
penup()
goto(200, 400)
pendown()
star(star_height, star_colour)






# Exit gracefully
hideturtle()
done()
