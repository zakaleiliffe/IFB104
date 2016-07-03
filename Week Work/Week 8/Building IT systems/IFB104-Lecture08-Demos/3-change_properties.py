#----------------------------------------------------------------
#
# Text colour changer
#
# This demonstration shows how a property of a
# widget can be changed dynamically, in this case
# its colour.
#

# Import the Tkinter functions
from Tkinter import *

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Change colour')

# Create a label widget which will be the widget whose
# property we change
changeable_label = Label(the_window, text = 'Choose a text colour',
                         font = ('Times', 48), fg = 'purple')

# Introduce the string variable whose value will be changed
# by selecting a radio button
label_colour = StringVar()

# Function to change the label's text colour when a radio
# button is selected
def change_colour():
    if label_colour.get() == 'r':
        changeable_label['fg'] = 'red'
    elif label_colour.get() == 'g':
        changeable_label['fg'] = 'green'
    else:
        changeable_label['fg'] = 'blue'

# Create a frame to hold the three radio buttons
colour_buttons = Frame(the_window)

# Create radio button widgets within the frame to control the
# label's colour
red_button = Radiobutton(colour_buttons, text = 'Red',
                         variable = label_colour, value = 'r',
                         command = change_colour)
green_button = Radiobutton(colour_buttons, text = 'Green',
                           variable = label_colour, value = 'g',
                           command = change_colour)
blue_button = Radiobutton(colour_buttons, text = 'Blue',
                          variable = label_colour, value = 'b',
                          command = change_colour)

# Put the three radio buttons into the frame (each on
# a separate grid row and sticking to the West border)
red_button.grid(row = 1, sticky = W)
green_button.grid(row = 2, sticky = W)
blue_button.grid(row = 3, sticky = W)

# Use the geometry manager to pack the two main widgets onto
# the window (with a small margin around them)
margin = 8 # pixels
changeable_label.pack(padx = margin, pady = margin)
colour_buttons.pack(padx = margin, pady = margin)

# Start the event loop to react to user inputs
the_window.mainloop()
