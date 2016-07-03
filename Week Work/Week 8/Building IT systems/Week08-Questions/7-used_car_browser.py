#--------------------------------------------------------------------------
#
#   Used Car Browser
#
#   In this exercise you will create a Graphical User Interface for
#   a database.  This is a non-trivial task that requires some mastery
#   of both Tkinter and SQL.
#
#   1) Before you begin you must import and run the "car_details.sql"
#   script via the phpMyAdmin interface.  This script creates a table
#   called "car_details" containing data about over 3,000 used cars for
#   sale.
#
#   2) Using the phpMyAdmin interface, create an SQL SELECT statement
#   which returns four columns from the "car_details" table,
#   the unique "CarId", the car's "make", the car's "model" and its
#   "price".  You will run this query from within your Tkinter code.
#
#   3) Below is some code which creates an empty Tkinter window.
#   Follow the instructions in this code to complete a program that
#   extracts relevant details from the database and displays them
#   in a scrollable Text widget to allow the user to browse just the
#   basic car details, without all the other distracting information
#   in the database table.
#


# Import the necessary Tkinter functions
from Tkinter import Tk, Text, END

# Import the MySQL-Python connector functions
from mysql.connector import *

# Create a window
window = Tk()

# Give the window a title
window.title('Used Car Browser')

###### ADD YOUR CODE TO CREATE WIDGETS AND THEIR BEHAVIOUR HERE

# 1. Define a function which accesses the "car_details" table
# and returns a list of all car identifiers, makes, models
# and prices (and nothing else).  Remember to close the
# connection to the the database at the end!
pass

# 2. Create a Text widget to display the results and pack
# it into the Tk window
pass

# 3. Call your function to get the relevant data from the
# car_details table and store the results set in a variable
pass

# 4. Insert each row in the results set into the "END" of
# the Text widget, one line each.  Format the result
# nicely so that it is easy to read the unique car
# identifier, make, model and price.
pass

# 5. Using your mouse's scroll wheel you should now be able to
# easily browse the details extracted from the database, to help
# you find a used car in your price range and of the type you
# prefer.  (Tk Text widgets are scrollable under Mac OS X.  You
# may find different behaviours on different operating
# systems.)

# Start the event loop to react to user inputs
window.mainloop()
