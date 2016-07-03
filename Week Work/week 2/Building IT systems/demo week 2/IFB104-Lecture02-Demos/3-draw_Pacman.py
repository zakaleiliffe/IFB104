#---------------------------------------------------------------------
#
# Demonstration - Draw Pacman
#
# As an introduction to drawing using Turtle graphics, here we'll
# draw a picture of the pioneering computer games character, Pacman.
# (Why Pacman? Because he's easy to draw!)
#
# Observation: To keep the code short we have "hardwired" all the
# measurements and angles in this program.  In general, however,
# this is not good coding practice, because it makes the program
# hard to change, e.g., if we wanted to change the size of the
# drawing.


# Import the Turtle graphics functions
from turtle import *

# Draw a black canvas
setup() # create window
title('Pacman') # put a title on the window
bgcolor('black') # make the background black

# Draw a huge yellow dot for Pacman's head
color('yellow')
dot(250)

# Draw a small black dot for Pacman's eye
penup()
color('black')
setheading(90) # point north
forward(65)
dot(40)

# Draw a black triangle to form Pacman's mouth
home()
setheading(30)
begin_fill() # start the filled-in region
forward(150)
right(120)
forward(150)
right(120)
forward(150)
end_fill() # end the filled-in region

# Finish the drawing
hideturtle() # hide the cursor
done() # release the drawing canvas so it can be closed
