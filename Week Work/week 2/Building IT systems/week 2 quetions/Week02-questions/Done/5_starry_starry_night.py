# Starry, starry night
#
# This exercise gives us some practice at creating graphics
# using random values.
#
# THE PROBLEM
#
# Draw the night sky as a black field containing 200 randomly-
# positioned white "stars" (dots), each of a randomly-chosen size.
# (The most realistic effect is achieved if the difference in
# sizes is only small.)
#
# Use the following problem-solving strategy:
#
# 1. Set up a drawing window of a known size
#    with a black background
# 2. Make the pen colour white and set the drawing
#    speed to "fastest"
# 3. Lift up the pen (so that you don't draw lines
#    between the stars)
# 4. Create a list of 200 "star numbers"
# 5. For each of the numbers in the list:
#    a. Choose a random x-y coordinate (being careful
#       that it is not off the edge of the screen)
#    b. Choose a random star size
#    c. Go to the location chosen
#    d. Draw a star (dot) of the chosen size
# 6. Hide the cursor and release the drawing window
#
# Hint: This is much easier than it sounds.  If you're not sure
# how to get started, use the "shooting gallery" demonstration
# program from the lecture as a guide.

# Import the necessary functions

from turtle import *
from random import randint

hideturtle()

screen_size = 600
setup(screen_size, screen_size)
# DEVELOP YOUR SOLUTION HERE

max_coord = screen_size / 2
min_star_size = 3
max_star_size = 10

#setting up screen size,window title, and color of background


title("Random Stars")
bgcolor("black")


#changing pen color to white and making drawing speed to 

pendown()
color("white")
speed("fastest")

#lift up the pen
penup()

#create a list of "200 star numbers"

star_numbers = range(200)

#for each star:

for star_num in star_numbers:
    # a. choose a random position on the screen
    star_pos_x = randint (-max_coord, max_coord)
    star_pos_y = randint (-max_coord, max_coord)
    # b. Choose a random size
    star_size = randint(min_star_size, max_star_size)
    goto (star_pos_x, star_pos_y)
    #Draw a dot of the chosen size
    dot(star_size)

done()
    



   
    
    
    
    
    
    





