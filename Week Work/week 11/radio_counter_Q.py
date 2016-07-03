#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no: 9499776
#  Student name: Tom Stark
#
#--------------------------------------------------------------------#

#----------------------------------------------------------------
#
# 5 labels and 5 radiobuttons (as per diagram)
# Initially, all labels are displayed in grey.
# When the user selects any one of the radiobuttons, the corresponding number
# of labels will display in green.
#----------------------------------------------------------------


# Import the Tkinter functions
from Tkinter import *

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Show Radio Count')

# PUT YOUR CODE HERE-------------------------------------------------#


#one label
one = Label(the_window,text="           ", bg="gray")
one.grid(row=0,column=0)

#two label
two = Label(the_window,text="           ", bg="gray")
two.grid(row=0, column=1)

#three label
three = Label(the_window,text="           ", bg="gray")
three.grid(row=0, column=2)

#four label
four = Label(the_window,text="           ", bg="gray")
four.grid(row=0, column=3)

#five label
five = Label(the_window,text="           ", bg="gray")
five.grid(row=0, column=4)



#Function to change colour of boxes 
def selectone():
    #one label
    one = Label(the_window,text="           ", bg="green")
    one.grid(row=0,column=0)
    #two label
    two = Label(the_window,text="           ", bg="gray")
    two.grid(row=0, column=1)
    #three label
    three = Label(the_window,text="           ", bg="gray")
    three.grid(row=0, column=2)
    #four label
    four = Label(the_window,text="           ", bg="gray")
    four.grid(row=0, column=3)
    #five label
    five = Label(the_window,text="           ", bg="gray")
    five.grid(row=0, column=4)

def selecttwo():
    #one label
    one = Label(the_window,text="           ", bg="green")
    one.grid(row=0,column=0)
    #two label
    two = Label(the_window,text="           ", bg="green")
    two.grid(row=0, column=1)
    #three label
    three = Label(the_window,text="           ", bg="gray")
    three.grid(row=0, column=2)
    #four label
    four = Label(the_window,text="           ", bg="gray")
    four.grid(row=0, column=3)
    #five label
    five = Label(the_window,text="           ", bg="gray")
    five.grid(row=0, column=4)

def selectthree():
    #one label
    one = Label(the_window,text="           ", bg="green")
    one.grid(row=0,column=0)
    #two label
    two = Label(the_window,text="           ", bg="green")
    two.grid(row=0, column=1)
    #three label
    three = Label(the_window,text="           ", bg="green")
    three.grid(row=0, column=2)
    #four label
    four = Label(the_window,text="           ", bg="gray")
    four.grid(row=0, column=3)
    #five label
    five = Label(the_window,text="           ", bg="gray")
    five.grid(row=0, column=4)

def selectfour():
    #one label
    one = Label(the_window,text="           ", bg="green")
    one.grid(row=0,column=0)
    #two label
    two = Label(the_window,text="           ", bg="green")
    two.grid(row=0, column=1)
    #three label
    three = Label(the_window,text="           ", bg="green")
    three.grid(row=0, column=2)
    #four label
    four = Label(the_window,text="           ", bg="green")
    four.grid(row=0, column=3)
    #five label
    five = Label(the_window,text="           ", bg="gray")
    five.grid(row=0, column=4)

def selectfive():
    #one label
    one = Label(the_window,text="           ", bg="green")
    one.grid(row=0,column=0)
    #two label
    two = Label(the_window,text="           ", bg="green")
    two.grid(row=0, column=1)
    #three label
    three = Label(the_window,text="           ", bg="green")
    three.grid(row=0, column=2)
    #four label
    four = Label(the_window,text="           ", bg="green")
    four.grid(row=0, column=3)
    #five label
    five = Label(the_window,text="           ", bg="green")
    five.grid(row=0, column=4)
    
    
    
#Create all radio buttons
v = IntVar()
#one radio
radioone= Radiobutton(the_window, text="One",value = 'one',command=selectone, variable=v)
radioone.grid(row=1,column=0)
#two radio
radiotwo= Radiobutton(the_window, text="Two",value = 'two',command=selecttwo, variable=v)
radiotwo.grid(row=1,column=1)
#three radio
radiothree= Radiobutton(the_window, text="Three",value = 'three',command=selectthree, variable=v)
radiothree.grid(row=1,column=2)
#four radio
radiofour= Radiobutton(the_window, text="Four",value = 'four',command=selectfour, variable=v)
radiofour.grid(row=1,column=3)
#five radio
radiofive= Radiobutton(the_window, text="Five",value = 'five',command=selectfive, variable=v)
radiofive.grid(row=1,column=4)


#----------------------------------------------------------------


# Start the event loop to react to user inputs
the_window.mainloop()
