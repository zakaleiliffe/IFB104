#---------------------------------------------------------------------
#
# Extending a class definition
#
# The program below defines a class of objects called Walkers, which
# pace around the screen in a square pattern.  It creates one
# such object and makes it take a fixed number of steps.
#
# This program is rather boring!  Your job is to make it more
# interesting by extending the class definition and its application
# in a number of ways.  Things you may consider doing include
# the following.
#
# * Extend the main program so that it creates multiple concurrent
#   walkers.
#
# * Add a method to the Walker class which allows the object's colour
#   to be changed, and extend the main program so the walkers change
#   colour periodically.
#
# * Create a subclass called Expanding_Walker whose objects get
#   bigger as they walk.  This could be done either by overriding
#   the "step" method or by adding a separate "grow" function.
#   The size of a turtle object can be changed with the "turtlesize"
#   method which accepts two integers, specifying the horizontal
#   and vertical sizes.
#


from turtle import *
from random import randint, choice

#----------
# The class from which "Walker" objects can be created
#
class Walker(Turtle):

    # This constructor accepts the walker's initial position
    # and heading and then sets local constants and
    # variables
    def __init__(self, x_pos, y_pos, heading):
        Turtle.__init__(self)
        self.penup()
        self.shape('circle')
        self.speed('slowest')
        self.goto(x_pos, y_pos)
        self.setheading(heading)
        self.__max_steps = 100 # max before turning
        self.__step_size = 4
        self.__step_count = 0

    # This method moves the walker along one step, turning
    # it ninety degrees after a fixed number of steps
    def step(self):
        if self.__step_count > self.__max_steps:
            self.left(90)
            self.__step_count = 0
        self.__step_count += 1
        self.forward(self.__step_size)


#----------
# This is the main program that creates and controls walkers

# Set up the drawing window
title("Walkers")
bgcolor("light yellow")

# Create a walker object and get it to take 1000 steps
walker_one = Walker(200, -200, 90)
for each in range(1000):
    walker_one.step()

# Release the window when finished
done()
            
        
        
