#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using Tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which some other value can be
# displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary Tkinter functions
from Tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')


##### PUT YOUR CODE HERE

# 1. Define a function to be called when the button is
#    pressed which will change the label's value

countdown = 10 

def button_pressed():
    if Label["text"] == "10":
        Label["text"] == "9"
        
    
        
    
   
        


# 2. Define the Button widget and pack it into the
#    main window

button(countdown_window, text = 'Push',
           command = button_pressed).pack()
 

# 3. Define the Label widget and pack it into the main
#    window
Label(countdown_window, text = "10".pack()

# Start the event loop to react to user inputs
countdown_window.mainloop()
