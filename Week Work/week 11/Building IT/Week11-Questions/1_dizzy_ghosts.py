#-----------------------------------------------------------------
#
# Dizzy Ghosts
#
# As an exercise in exploiting object orientation for concurrency,
# here you will develop a program with multiple turtle graphics
# objects appearing to move simultaneously.
#
# So far all of our turtle graphics programs have involved only
# a single default drawing cursor ("turtle") which limits
# what we can do.  However Turtle (with a capital "T") is actually
# a class, meaning that we can instantiate multiple objects from
# it so that we can have several "turtles" appear on the
# screen at the same time.
#
# Enclosed with this file are four "ghost" icons, each of them
# being one of the four ghosts from PacMan.  (These images have
# black backgrounds, so we should display them on a black screen.)
#
# Your task is to create a program in which all four ghosts appear
# on the screen simultaneously.  To do this you will need to
# instantiate four distinct objects and get each of them to move
# in turn.  (We will not attempt to do this elegantly;
# a brute-force hardwired solution is adequate.)
#
# Hints - Some of the Turtle features you will find helpful are
# as follows:
#
# * Turtle() - a class from which you can create turtle objects
# * register_shape() - a function for making GIF files known to
#   the program
# * t.shape() - a method that defines the shape of Turtle object
#   "t", where the shape can be a GIF image (that has been
#   registered)
# * Similarly, other turtle graphics functions that you have already
#   used for moving and drawing, such as "penup", "speed", "goto",
#   "forward", "circle", "hideturtle", etc, can be called as methods on
#   individual objects
#


#------------------------------------------------------------------
# Import the necessary pre-defined functions.
from turtle import *


#------------------------------------------------------------------
# Main program starts here:
#


# 1. Set up the drawing window.
title("Dizzy Ghosts")
bgcolor("black") # to match the icons' backgrounds


# 2. Register the four icons.
register_shape("ghost_blue.gif")
register_shape("ghost_red.gif")
register_shape("ghost_orange.gif")
register_shape("ghost_pink.gif")


# 3. Instantiate the four ghost objects as instances
#    of the Turtle class, then define
#    their shapes, and move them to distinct starting
#    positions.  It's also a good idea to set their
#    drawing speeds to "fastest".

##### *** PUT YOUR CODE FOR CREATING GHOST OBJECTS HERE
blueGhost.Turtle()
redGhost.Turtle()
orangeGhost.Turtle()
pinkGhost.Turtle()

# 4. Make all four ghosts draw circles a fixed number
#    of times.  To give the impression that all four are
#    moving at the same time, it's helpful to just draw
#    part of a circle in each step.  The "extent"
#    parameter to the "circle" method allows you to specify
#    how much of the circle to draw at each step (in degrees).

##### *** PUT YOUR CODE FOR MOVING GHOST OBJECTS HERE


# 5. Make the ghosts disappear when finished.

##### *** PUT YOUR CODE FOR MAKING GHOST OBJECTS INVISIBLE HERE


# 6. Release the drawing window when finished.
done()
