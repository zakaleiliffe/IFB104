#---------------------------------------------------------------------
#
# Ants Nest
#
# As an example of the way object-orientation allows us to maintain
# several independent objects, each with its own attributes, here we
# create a simple simulation in which several Turtle graphics objects
# appear on the screen at the same time.
#
# The scenario is that you've disturbed an ants nest and the worker
# ants come rushing out to defend it.  The nest is represented by a
# black dot in the middle of the screen and each ant will be represented
# by the default Turtle cursor icon.  The ants all walk out of the nest
# in a straight line.  Importantly, however, each ant has its own "step
# size" and "orientation", so they will all walk in different directions
# at different speeds.
#
# Your task is to complete the missing code below.  You must:
#
# 1) Complete two methods in the Ant class which define how
#    ants are initialised and how they walk, respectively.
#
# 2) Fill in the code in the main program for creating and moving
#    the whole nest of ants.
#
# Extra exercise: Extend your program so that, having scared off the
# threat, the ants all turn around and return to their hole.  To do
# so you will need to add another method to the class so that the
# ant objects can be made to rotate 180 degrees.
#


# Import the necessary pre-defined functions.
from turtle import *
from random import randint


#----------
# A class which defines the behaviour of a single
# ant, from which we can create many ants
class Ant:

    # Constructor to create a new Turtle object representing
    # an ant (Hint: Remember that variables belonging to a
    # class must be preceded by "self.")
    def __init__(self, step_size, orientation):
        pass
    
        ##### PUT YOUR CODE FOR CONSTRUCTING THIS ANT HERE
    

    # Method to move this ant forward one step
    def walk(self):
        pass

        ##### PUT YOUR CODE FOR MOVING THIS ANT FORWARD BY ONE STEP HERE



#----------
# A main program to create the Ant objects and cause them
# to move

# 0. Constants
number_of_ants = 20
min_step, max_step = 3, 10 # pixels
number_of_steps = 50

# 1. Set up the drawing window
title("Ants Nest")
bgcolor('green')

# 2. Draw the ant nest (using the default turtle object)
color('black')
dot(25)

# 3. Create lots of ants, each with their own step size and
#    orientation (Hint: Use a list to hold all the ant objects)

##### PUT YOUR CODE FOR CREATING ALL OF THE ANT OBJECTS HERE


# 4. Move each of the ants in turn, up to a fixed number of
#    steps

##### PUT YOUR CODE FOR MOVING ALL OF THE ANTS MULTIPLE TIMES HERE


# 5. Release the drawing window
done()
