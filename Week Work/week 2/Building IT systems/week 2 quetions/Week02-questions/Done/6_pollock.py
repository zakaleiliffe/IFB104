##  Jackson Pollock's Final Masterpiece
##
##  20th century "artists" such as Jackson Pollock achieved fame
##  by stumbling drunkenly around a canvas on the floor
##  dribbling paint out of tins.  Today we can achieve the same
##  effect without getting our hands dirty using Python!
##  
##  Using Turtle graphics develop a program to draw many blobs 
##  (dots) of random colour, size and location on the screen.
##  The blobs should be connected by lines of "paint" of
##  various widths as if paint had been dribbled from one
##  blob to the next.  The "paint" should not go off the edge
##  of the "canvas".  Use the following solution strategy.
##
##    1. Set up the blank canvas of a known size
##    2. Ensure the pen is down
##    3. Create a list of "blob" numbers
##    4. For each blob number in the list:
##       a. Set a random pen colour
##       b. Pick a random pen width
##       c. Go to a random location on the screen
##          (drawing as you go)
##       d. Draw a blob (dot)
##    5. Exit the program gracefully
##
##  Hint: To get a wide range of colours, note that Turtle's
##  "color" function can accept three numbers as parameters,
##  representing red-green-blue pixel densities.  These
##  numbers are floating point values between 0.0 and 1.0.
##  Also recall that the "random" module's "uniform" function
##  produces a random floating point number.
##
##  Note that this exercise is actually very similar to the
##  previous "Starry, Starry Night" one, so you can develop
##  your solution as an extension of that.


# Import the functions required
from turtle import *
from random import uniform, randint


## DEVELOP YOUR PROGRAM HERE

#some fixed properties
max_coord = 300 #painting limits, in pixels
max_blob_size = 20
max_dribble_width = 8

#set up the "canvas"

setup(max_coord * 2, max_coord * 2)
title("Jackson Pallock's final masterpiece")

#paint quickly
speed('fastest')

#put the pen down

pendown()

#create a list of blob numbers
blob_numbers = range(300)

# Generate a large number of paint blobs
for blob_num in blob_numbers:

    #set the blob colour using randomly selected
    #RGB values between  0.0 and 1.0
    color(uniform(0.0, 1.0), uniform(0.0, 1.0), uniform(0.0, 1.0))
    #pick a random pen width
    width(randint(1, max_dribble_width))

    #Go to the location for the next blob, dribbling
    #paint as we go
    goto(randint(-max_coord, max_coord),
         randint(-max_coord, max_coord)


    #draw a 'blob' of a random diameter
    #dot(randint(1, max_blob_size))

#Exit


hideturtle()
done()








