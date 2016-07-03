#----------------------------------------------------------------
#
# Placement demo
#
# A simple demonstration of using the place manager to
# arrange several widgets into a particular pattern
# (adapted from Y. Liang, "Introduction to Programming
# using Python").
#
# Note that the precise appearance of this window will
# depend on your screen resolution, for which reason the
# place manager is best avoided unless you really need
# to put things at specific pixel locations.
#

# Import the Tkinter functions
from Tkinter import *

# Create a window
place_window = Tk()

# Give the window a title
place_window.title('Placement demo')

# Create three coloured widgets
red_label = Label(place_window, text = 'Red', bg = 'red',
                  width = 5, font = ('Arial', 24))
blue_label = Label(place_window, text = 'Blue', bg = 'blue',
                   width = 5, font = ('Arial', 24))
green_label = Label(place_window, text = 'Green', bg = 'green',
                    width = 5, font = ('Arial', 24))

# Place the three rectangles diagonally across the window
red_label.place(x = 20, y = 20)
blue_label.place(x = 50, y = 50)
green_label.place(x = 80, y = 80)

# Start the event loop (although this code doesn't react to
# any events)
place_window.mainloop()
