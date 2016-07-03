#-------------------------------------------------------------------------
#
#  Olympic Rings
#
#  In this folder you will find a file "olympic_rings.pdf" which shows
#  the flag used for the Olympics since 1920.  Notice that this flag
#  consists of five rings that differ only in their position and colour.
#  If we want to draw it using Turtle graphics it would therefore be
#  a good idea to define a function that draws one ring and reuse it
#  five times.
#
#  Complete the code below to produce a program that draws a reasonable
#  facsimile of the Olympic flag.  (NB: In the real flag the rings are
#  interlocked.  Don't try to reproduce this tricky feature, just draw
#  rings that overlap.)
#


#-------------------------------------------------------------------------
#  Step 1: Function definition
#
#  Define a function called "ring" that takes three parameters, an
#  x-coordinate, a y-coordinate and a colour.  When called this function
#  should draw an "olympic ring" of the given colour centred on the
#  given coordinates.  (Note that Turtle graphic's "circle" function
#  draws a circle starting from the cursor's current position, not
#  centred on the cursor's position.)  Since all the circles are the
#  same size you can define the radius and thickness of the circle
#  within the function.

###  PUT YOUR FUNCTION DEFINITION HERE
from turtle import *

setup(1000, 650)
title('"... and it\'s gold, Gold, GOLD for Australia!"')

speed("fast")


def ring(radius, colour):
    
    width(10)      #width of turtle
    color(colour)    #colour will be colour chosen in parameters
    radius = radius
    setheading(90)
    pendown()
    circle(80)
    penup()
segment_numbers = range(1)



penup()
goto(-150, 100)
for seg_no in segment_numbers:
    pendown()
    ring(80, "blue")

penup()
goto(40, 100)

for seg_no in segment_numbers:
    pendown()
    ring(80, "black")





penup()
goto(230, 100)

for seg_no in segment_numbers:
    pendown()
    ring(80, "red")



penup()
goto(-55, 20)

for seg_no in segment_numbers:
    pendown()
    ring(80, "yellow")    



penup()
goto(135, 20)

for seg_no in segment_numbers:
    pendown()
    ring(80, "green")
    








        
        
    
            
    
    
hideturtle()
done()    
    

#-------------------------------------------------------------------------
#  Step 2: Calling the function
#
#  Now write code to call the function five times, each time with
#  different coordinates and colours, to create the flag.  To get
#  you started we have provided some of the Turtle framework.

#  Import the Turtle functions 



#  Create the drawing window



# Draw the five rings

###  PUT YOUR FUNCTION CALLS HERE




    









#  Shut down the drawing window

