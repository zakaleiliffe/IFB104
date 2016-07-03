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
ghost_red = Turtle()
ghost_red.shape("ghost_red.gif")
ghost_red.penup()
ghost_red.goto(100, 100)
ghost_red.speed("fastest")

ghost_blue = Turtle()
ghost_blue.shape("ghost_blue.gif")
ghost_blue.penup()
ghost_blue.goto(100, -100)
ghost_blue.speed("fastest")

ghost_pink = Turtle()
ghost_pink.shape("ghost_pink.gif")
ghost_pink.penup()
ghost_pink.goto(-100, 100)
ghost_pink.speed("fastest")

ghost_orange = Turtle()
ghost_orange.shape("ghost_orange.gif")
ghost_orange.penup()
ghost_orange.goto(-100, -100)
ghost_orange.speed("fastest")


# 4. Make all four ghosts draw circles a fixed number
#    of times.  To give the impression that all four are
#    moving at the same time, it's helpful to just draw
#    part of a circle in each step.  The "extent"
#    parameter to the "circle" method allows you to specify
#    how much of the circle to draw at each step (in degrees).
for each in range(200):
    ghost_red.circle(30, 20)
    ghost_blue.circle(20, 45)
    ghost_orange.circle(40, 90)
    ghost_pink.circle(50, 40)


# 5. Make the ghosts disappear when finished.
ghost_red.hideturtle()
ghost_blue.hideturtle()
ghost_orange.hideturtle()
ghost_pink.hideturtle()


# 6. Release the drawing window when finished.
done()
