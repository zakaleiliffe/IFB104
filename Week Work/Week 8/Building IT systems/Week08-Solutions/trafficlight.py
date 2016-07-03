#----------------------------------------------------------------
#
# TRAFFIC LIGHT
#
# In this exercise you must create a Graphical User
# Interface using Tkinter.  The program should create
# a window containing a drawing canvas and three buttons.
# Each time one of the buttons is pressed a red, yellow
# or green circle should be drawn on the canvas, in
# imitation of a traffic light.
#
# As an additional feature, you could restrict the
# buttons so that the lights can only follow the usual
# green-yellow-red-green sequencing.  (There is no yellow
# between red and green in real traffic lights!)
#

# Import the necessary Tkinter functions
from Tkinter import Tk, Button, Canvas

# Create a window
traffic_window = Tk()

# Give the window a title
traffic_window.title('Traffic Light')

# Functions to execute when the buttons are pressed (with
# no restrictions in this case, but you could introduce a
# global variable to keep track of the current colour and
# only allow changes if the green-yellow-red-green sequencing
# is followed)
def red_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'red')
def yellow_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'yellow')
def green_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'green')

# Create the three button widgets
red_button = Button(traffic_window, text = 'Red',
                    width = 6, command = red_light)
yellow_button = Button(traffic_window, text = 'Yellow',
                       width = 6, command = yellow_light)
green_button = Button(traffic_window, text = 'Green',
                      width = 6, command = green_light)

# Create the drawing canvas
traffic_light = Canvas(traffic_window, width = 200,
                       height = 200, bg = 'white')

# Call the geometry manager to place the widgets onto
# the window (in a grid arrangement, with a margin)
margin_size = 5
traffic_light.grid(padx = margin_size, pady = margin_size,
                   row = 0, column = 0, columnspan = 3)
green_button.grid(pady = margin_size, row = 1, column = 2)
yellow_button.grid(pady = margin_size, row = 1, column = 1)
red_button.grid(pady = margin_size, row = 1, column = 0)

# Start the event loop to react to user inputs
traffic_window.mainloop()
