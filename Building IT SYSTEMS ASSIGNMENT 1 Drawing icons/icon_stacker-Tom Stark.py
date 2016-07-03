
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 9499776
#    Student name: Tom Stark

#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  ICON STACKING
#
#  This task tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_icons".
#  You are required to complete this function so that when the
#  program is run it produces an image of multiple icons packed into
#  a rectangular frame, using data stored in a list to determine the
#  positions and orientations of the icons.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the grid.  You should not change any of
# the code in this section.
#

# Import the functions needed to complete this task.  You should
# not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing window.  Do not change any of these values.

frame_width = 900 # the width of the grid frame in pixels
frame_height = 600 # the height of the grid frame in pixels
margin = 100 # size of the margin around the frame in pixels
window_height = frame_height + margin
window_width = frame_width + 2 * margin
num_columns = 6 # number of columns in the grid frame
num_rows = 4 # number of rows in the grid frame
square_width = frame_width / num_columns # width of each square
square_height = frame_height / num_rows # height of each square

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Grid---------------------------------#
#
# The functions in this section are called by the main program to
# draw the grid.  You should not change any of the code in this
# section.  Note that each of these functions leaves the pen up.
#

# Draw the the rectangular frame that contains all the icons
def draw_frame(frame_on = True):

    # Only draw the rectangle if the argument is True
    if frame_on:

        penup()
        goto(-frame_width/2, -frame_height/2) # start at the bottom-left
        setheading(90) # face north
        pendown() 
        forward(frame_height)
        right(90) # face east
        forward(frame_width)
        right(90) # face south
        forward(frame_height)
        right(90) # face west
        forward(frame_width)
        penup()


# Draw the individual squares in the grid
def draw_squares(squares_on = True):

    # Only draw the squares if the argument is True
    if squares_on:
    
        dot_size = 3 # the size of the dots, in pixels
        dot_gap = 15 # separation of dots, in pixels

        # Don't draw connecting lines
        penup()
        
        # Draw dotted vertical grid lines
        color('yellow')
        for x_coord in range(-(frame_width/2 - square_width), frame_width/2, square_width):
            # Draw a dotted vertical line
            for point in range(-frame_height/2 + dot_gap, frame_height/2, dot_gap):
                goto(x_coord, point)
                dot(dot_size)

        # Draw dotted horizontal grid lines
        for y_coord in range(-(frame_height/2 - square_height), frame_height/2, square_height):
            # Draw a dotted horizontal line
            for point in range(-frame_width/2 + dot_gap, frame_width/2, dot_gap):
                goto(point, y_coord)
                dot(dot_size)

        # Draw a black dot in the exact centre of the grid to
        # mark the "home" coordinate
        home()
        color('black')
        dot(dot_size)


# Draw the numeric x-y labels
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        label_gap = 15 # separation of labels from the frame, in pixels
        font_size = 16 # size of characters for the labels

        # Don't draw connecting lines
        penup()
        
        # Draw the x axis labels
        goto(-(frame_width - square_width)/2, -(frame_height/2 + label_gap + font_size))
        setheading(0) # face east
        for x_label in range(num_columns):
           write(str(x_label), align = 'center', font=('Arial', font_size, 'bold'))
           forward(square_width)

        # Draw the y axis labels
        goto(-(frame_width/2 + label_gap), -(frame_height - square_height)/2)
        setheading(90) # face north
        for y_label in range(num_rows):
           write(str(y_label), align = 'center', font=('Arial', font_size, 'bold'))
           forward(square_width)

#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list containing the specifications
# for the position and orientation of several icons to display
# in the grid.  Each data set element specifies how to display
# one icon using four values:
#
#    [icon_style, bottom_left_column, bottom_left_row, orientation]
#
# There are four icon styles, named 'A', 'B', 'C' and 'D'.  The
# icons each have different x-y sizes, expressed in grid squares:
#
#     A - 1x1
#     B - 1x2
#     C - 2x2
#     D - 2x3
#
# The column and row coordinates say in which grid square to place
# the bottom-left corner of the icon (taking into consideration its
# orientation).  The orientation specifies the direction in which
# the top of the icon should point, 'N', 'S', 'E' or 'W'.  For
# instance, an icon pointing North should appear upright, whereas
# the same icon pointing South should appear upside-down.
#

# The following data set doesn't specify drawing any icons at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_icons" function.

data_set_00 = []

# The following data sets each draw just one of the icons but with
# different orientations.  You can use them to test your icon drawing
# code individually.  (There are two data sets for the 2x3 icon D
# because it's too big to fit in the frame in all four orientations.)

data_set_01 = [['A', 1, 0, 'N'], ['A', 2, 1, 'E'], ['A', 3, 2, 'S'], ['A', 4, 3, 'W']]

data_set_02 = [['B', 2, 0, 'W'], ['B', 2, 3, 'E'], ['B', 1, 1, 'N'], ['B', 4, 1, 'S']]

data_set_03 = [['C', 0, 0, 'N'], ['C', 1, 2, 'E'], ['C', 3, 0, 'S'], ['C', 4, 2, 'W']]

data_set_04a = [['D', 0, 0, 'N'], ['D', 2, 2, 'E'], ['D', 3, 0, 'W']]

data_set_04b = [['D', 0, 2, 'E'], ['D', 1, 0, 'W'], ['D', 4, 1, 'S']]

# The next group of data sets completely fill the grid with icons of
# different types and orientations.  You will need to have all of your
# icon drawing code working to use them.  If your code is working
# correctly using any of these data sets will completely fill the
# frame with non-overlapping icons.

# All four icons, arranged symmetrically, all upright (pointing North)
data_set_05 = [['A', 0, 2, 'N'], ['A', 0, 3, 'N'], ['A', 2, 0, 'N'],
               ['A', 3, 0, 'N'], ['A', 5, 2, 'N'], ['A', 5, 3, 'N'],
               ['B', 1, 2, 'N'], ['B', 4, 2, 'N'],
               ['C', 0, 0, 'N'], ['C', 4, 0, 'N'],
               ['D', 2, 1, 'N']]

# All four icons, asymmetric arrangement, all upright (pointing North)
data_set_06 = [['A', 1, 3, 'N'], ['A', 2, 3, 'N'], ['A', 3, 1, 'N'],
               ['A', 3, 0, 'N'], ['A', 5, 2, 'N'], ['A', 5, 3, 'N'],
               ['B', 0, 0, 'N'], ['B', 0, 2, 'N'],
               ['C', 3, 2, 'N'], ['C', 4, 0, 'N'],
               ['D', 1, 0, 'N']]

# The same as above but with all icons upside down (pointing South)
data_set_07 = [['A', 1, 3, 'S'], ['A', 2, 3, 'S'], ['A', 3, 1, 'S'],
               ['A', 3, 0, 'S'], ['A', 5, 2, 'S'], ['A', 5, 3, 'S'],
               ['B', 0, 0, 'S'], ['B', 0, 2, 'S'],
               ['C', 3, 2, 'S'], ['C', 4, 0, 'S'],
               ['D', 1, 0, 'S']]

# All four icons in different orientations
data_set_08 = [['A', 5, 0, 'N'], ['A', 5, 1, 'S'], ['A', 5, 2, 'E'], ['A', 5, 3, 'W'],
               ['B', 2, 0, 'S'], ['B', 3, 0, 'E'],
               ['C', 0, 0, 'W'],
               ['D', 0, 2, 'E'], ['D', 3, 1, 'N']]


# Another arrangement with all four icons in different orientations
data_set_09 = [['A', 0, 0, 'E'], ['A', 0, 1, 'N'], ['A', 1, 3, 'S'], ['A', 2, 3, 'W'], 
               ['B', 0, 2, 'N'], ['B', 5, 2, 'S'], ['B', 5, 0, 'N'],
               ['C', 3, 0, 'N'], ['C', 3, 2, 'E'],
               ['D', 1, 0, 'S']]

# Yet another arrangement with all four icons in different orientations
data_set_10 = [['A', 0, 0, 'E'], ['A', 0, 1, 'N'], ['A', 2, 2, 'S'], ['A', 2, 3, 'W'], 
               ['B', 0, 3, 'E'], ['B', 0, 2, 'W'], ['B', 5, 2, 'N'],
               ['C', 1, 0, 'N'], ['C', 3, 2, 'E'],
               ['D', 3, 0, 'W']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#

def draw_icon(data_set):
    for data in data_set:
        penup()
        # go to the column number where the icon's bottom-left corner must appear
        x = 0
        if data[1] == 0:         ###These statements say that if the value at position
                                    #[1] in the list of list == the value of the column number
                                    #it will select the corresponding x coordinate for that number 
            x = -450
        elif data[1] == 1:
            x = -300
        elif data[1] == 2:
            x = -150
        elif data[1] == 3:
            x = 0
        elif data[1] == 4:
            x = 150
        elif data[1] == 5:
            x = 300
        else:
            print "Invalid column value"

        # choose the row number                 ###These statements say that if the value at position
                                    #[2] in the list of list == the value of the row number
                                    #it will select the corresponding y coordinate for that number 
        if data[2] == 0:
            y = -300
        elif data[2] == 1:
            y = -150
        elif data[2] == 2:
            y = 0
        elif data[2] == 3:
            y = 150
        else:
            print "Invalid row value" 
        

        
        goto(x, y)               ##This is the result of the above 2 if statements ( the turtle moves to this
                                ## postion ready to read the next chunk of "if" statements. 

        #set the orientation of the icon
        setheading(0) #sets heading to default
        if data[0] == 'A' and data[3] == 'N':
            pass
        elif data[0] == 'A' and data[3] == 'E':
            left(90)
            forward(150)
            right(180)
        elif data[0] == 'A' and data[3] == 'S':
            left(90)
            forward(150)
            right(90)
            forward(150)
            left(180)                                       ###These "if" statements with the "and" operator rotates the
                                                            ##icon to the required orientation.  
        elif data[0] == 'A' and data[3] == 'W':
            forward(150)
            left(90)
            ######


        elif data[0] == 'B' and data[3] == 'N':
            pass
        elif data[0] == 'B' and data[3] == 'E':
            left(90)
            forward(150)
            right(180)
        elif data[0] == 'B' and data[3] == 'S':
            left(90)
            forward(300)
            right(90)
            forward(150)
            left(180)
        elif data[0] == 'B' and data[3] == 'W':
            forward(300)
            left(90)
        ##########
        elif data[0] == 'C' and data[3] == 'N':
            pass
        elif data[0] == 'C' and data[3] == 'E':
            left(90)
            forward(300)
            right(180)
        elif data[0] == 'C' and data[3] == 'S':
            left(90)
            forward(300)
            right(90)
            forward(300)
            left(180)
        elif data[0] == 'C' and data[3] == 'W':
            forward(300)
            left(90)
        ##########
        elif data[0] == 'D' and data[3] == 'N':
            pass
        elif data[0] == 'D' and data[3] == 'E':
            left(90)
            forward(300)
            right(180)
        elif data[0] == 'D' and data[3] == 'S':
            left(90)
            forward(450)
            right(90)
            forward(300)
            left(180)
        elif data[0] == 'D' and data[3] == 'W':
            forward(450)
            left(90)
            
        else:
            print "Incorrect orientation"
        
        
# Choose the logo to print
        if data[0] == 'A':
            twitter()
        elif data[0] == 'B':
            facebook()
        elif data[0] == 'C':
            snapchat()
        elif data[0] == 'D':
            instagram()
        else:
            print "Incorrect icon letter"
        
            
    
def twitter():      #1 x 1
    #Draw light Blue BG
    penup()
    width(1)
    forward(10)
    pendown()
    color('#00BDFF')
    begin_fill()
    forward(130)
    circle(10, 90)
    forward(130)
    circle(10, 90)
    forward(130)
    circle(10, 90)
    forward(130)
    circle(10, 90)
    end_fill()
    #Draw bird
    color('white')
    penup()
    forward(70)
    left(100)
    forward(30)
    right(95)
    pendown()
    begin_fill()
    circle(60, 90)
    right(60)
    circle(300, 3)
    left(140)
    circle(300, 4)
    left(220)
    circle(300, 5)
    left(150)
    circle(300, 3)
    right(90)
    circle(20, 180)
    right(120)
    circle(-120, 30)
    left(90)
    circle(25, 120)
    right(180)
    circle(300, 4)
    left(120)
    circle(60, 30)
    right(310)
    circle(20, -40)
    right(90)
    circle(20, 90)
    right(150)
    circle(-80, 22)
    left(150)
    circle(55, 68)
    end_fill()


def facebook(): # 1 x 2
    #Draw Blue BG
    penup()
    forward(10)
    pendown()
    color("Blue")
    begin_fill()
    forward(130)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    forward(130)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    end_fill()
    #Draw F
    penup()
    color("white")
    forward(65)     #Bottom of "F"
    left(90)
    begin_fill()
    pendown()
    forward(190) #height of F
    left(90)
    forward(25)
    right(90)
    forward(22)
    right(90)
    forward(25)
    left(90)
    forward(30) 
    circle(-20 ,90)
    forward(25)
    right(90)
    forward(23)
    right(90)
    forward(16)
    circle(8, 90)
    forward(18)
    left(90)
    forward(25)
    right(94)
    forward(22)
    right(86)
    forward(22)
    left(90)
    forward(192) #height of F
    right(90)
    forward(25)
    end_fill()

def snapchat():     # 2 x 2
    #Draw Yellow BG
    penup()
    forward(10)
    pendown()
    color("yellow")
    begin_fill()
    forward(280)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    end_fill()
    #Draw Ghost (moving to position
    width(7)
    color("black")
    penup()
    right(0)
    forward(160)
    left(90)
    forward(215)
    left(90)
    forward(80)
    #Draw ghost
    fillcolor("white")
    begin_fill()####
    pendown()
    right(90)
    circle(-70, 180)
    forward(30)
    right(90)
    circle(-20, -40)
    circle(8, -190)
    right(180)
    forward(20)
    circle(10, 80)
    circle(300, 20)
    circle(-10, 120)
    circle(-400, 5)
    left(65)
    forward(18)
    right(90)
    circle(100, 7) 
    circle(40, 10)
    left(50)
    circle(-73, 99)
    right(-90)
    forward(18)
    right(95)
    forward(18)
    circle(40, 10)
    left(60)
    circle(-100, 25)
    circle(-10, 120)
    circle(300, 20)
    circle(10, 80)
    forward(20)
    right(180)
    circle(8, -190)
    circle(-20, -40)
    right(92)
    forward(40)
    end_fill()


def instagram():     ### 2 x 3
    #Draw whitish BG
    penup()
    forward(10)
    pendown()
    color("#FEEFC8")
    begin_fill()
    forward(280)
    circle(10, 90)
    forward(430)
    circle(10, 90)
    forward(280)
    circle(10, 90)
    forward(430)
    circle(10, 90)
    end_fill()
    #draw top brown square
    color("#422000")
    penup()
    forward(290)
    left(90)
    forward(350)
    left(90)
    begin_fill()
    pendown()
    forward(300)
    right(90)
    forward(90)
    circle(-10, 90)
    forward(280)
    circle(-10, 90)
    forward(90)
    end_fill()
    ## black line under the brown rectangle
    right(90)
    width(2)
    color("black")
    forward(300)
    penup()
    right(180)
    forward(30)
    left(90)
    ## red stripe
    pendown()
    begin_fill()
    color("red")
    forward(98)
    right(90)
    forward(10)
    right(90)
    forward(98)
    right(90)
    forward(10)
    end_fill()
    penup()
    ##yellow stripe
    right(180)
    forward(10)
    left(90)
    pendown()
    begin_fill()
    color("yellow")
    forward(98)
    right(90)
    forward(10)
    right(90)
    forward(98)
    right(90)
    forward(10)
    end_fill()
    ##green stripe
    color("#2DEF96")
    penup()
    right(180)
    forward(10)
    left(90)
    pendown()
    begin_fill()
    forward(98)
    right(90)
    forward(10)
    right(90)
    forward(98)
    right(90)
    forward(10)
    end_fill()
    ##blue stripe
    color("#2D85FF")
    penup()
    right(180)
    forward(10)
    left(90)
    pendown()
    begin_fill()
    forward(98)
    right(90)
    forward(10)
    right(90)
    forward(98)
    right(90)
    forward(10)
    end_fill()
    penup()
    ## Draw camera lens
    color("black")
    left(90)
    forward(150)
    left(90)
    forward(90)
    pendown()
    width(2)
    color("black")
    fillcolor("white")
    begin_fill()
    circle(80)
    end_fill()
    ## Draw camera lens
    penup()
    left(90)
    forward(8)
    right(90)
    pendown()
    color("#201D16")
    begin_fill()   
    circle(72)
    end_fill()
    ## Draw other camera lens
    penup()
    left(90)
    forward(230)
    right(90)
    forward(80)
    pendown()
    fillcolor("#201D16")
    begin_fill()
    forward(40)
    circle(-20, 90)
    forward(40)
    circle(-20, 90)
    forward(40)
    circle(-20, 90)
    forward(40)
    circle(-20, 90)
    end_fill()
    ##
    penup()
    color("black")
    right(90)
    forward(40)
    right(90)
    forward(4)
    left(90)
    pendown()
    fillcolor("#25101A")
    begin_fill()
    circle(25)
    end_fill()
    ##
    penup()
    forward(90)
    right(90)
    forward(75)
    pendown()
    fillcolor("#25101A")
    begin_fill()
    circle(30)
    end_fill()
    ###
    penup()
    color("#5B5B5B")
    right(90)
    forward(55)
    left(90)
    forward(90)
    pendown()
    begin_fill()
    forward(30)
    circle(15, 180)
    forward(30)
    circle(15, 180)
    end_fill()
    ## THE "I"
    penup()
    color("white")
    forward(10)
    left(90)
    forward(7)
    right(90)
    forward(18)
    pendown()
    forward(8)
    right(180)
    forward(4)
    right(90)
    forward(15)
    right(90)
    penup()
    forward(4)
    right(180)
    pendown()
    forward(8)
    ## THE "N"
    penup()
    forward(5)
    pendown()
    left(90)
    forward(6)
    circle(2, 180)
    forward(6)
    ## THE "S"
    penup()
    left(90)
    forward(7)
    pendown()
    circle(4, 170)
    circle(-2, 195)
    ## DRAW "t"
    penup()
    forward(15)
    right(85)
    forward(10)
    right(155)
    pendown()
    forward(20)
    penup()
    right(180)
    forward(4)
    left(90)
    pendown()
    forward(5)
    penup()
    left(180)
    forward(5)
    pendown()
    forward(5)
    ## Draw "a"
    penup()
    right(180)
    forward(15)
    pendown()
    forward(4)
    circle(-4, 93)
    forward(12)
    right(180)
    forward(2)
    left(110)
    circle(-5, 200)
    color("black")
    

#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the grid, ready for you to start drawing
# your icons.  Do not change any of this code except where indicated
# by comments marked '*****'.
#
    
# Set up the drawing window with a neutral background colour and
# enough space for the grid
setup(window_width, window_height)
bgcolor('grey')

# Give the window a title
# ***** Replace this title with one that describes your chosen
# ***** theme and icons
title('Social Media Icons(FaceBook, Snapchat, Twitter, Instagram)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('very fast')

# Draw the grid
# ***** If you want to turn off animation while drawing the grid,
# ***** change the following argument to False
tracer(False)
# ***** If you don't want to display the grid's frame, individual
# ***** squares or the numeric labels change the corresponding
# ***** argument(s) below to False
draw_frame(True)
draw_squares(True)
draw_labels(True)

# Call the student's function to display the icons
# ***** If you want to turn off animation while drawing your icons,
# ***** change the following argument to False
tracer(True)
# ***** Change the argument to this function to test your
# ***** code with different data sets

draw_icon(data_set_10)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#
