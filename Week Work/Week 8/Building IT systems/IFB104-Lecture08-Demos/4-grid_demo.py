#----------------------------------------------------------------
#
# Grid demo
#
# A simple demonstration of using the grid manager to
# arrange several widgets into a particular pattern
# (adapted from Y. Liang, "Introduction to Programming
# using Python")
#

# Import the Tkinter functions
from Tkinter import *

# Create a window
grid_window = Tk()

# Give the window a title
grid_window.title('Grid demo')

# Create a text message that spans the first two columns
# and is three rows high
message = Message(grid_window,
                  text = 'Enter your name, but do not expect a response')
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)

# Put a label and a text entry box in the first row, columns
# 3 and 4, with the text entry box being the default input "focus"
first_name_label = Label(grid_window, text = 'First name:', justify = RIGHT)
first_name_entry = Entry(grid_window, width = 10)
first_name_label.grid(row = 1, column = 3)
first_name_entry.grid(row = 1, column = 4)
first_name_entry.focus()

# Put a label and a text entry box in the second row, columns
# 3 and 4
surname_label = Label(grid_window, text = 'Surname:', justify = RIGHT)
surname_entry = Entry(grid_window, width = 10)
surname_label.grid(row = 2, column = 3)
surname_entry.grid(row = 2, column = 4)

# Put a button in the third row, column 4
done_button = Button(grid_window, text = 'Done', takefocus = False)
done_button.grid(row = 3, column = 4, sticky = E)

# Start the event loop (although this code doesn't react to
# any events)
grid_window.mainloop()
