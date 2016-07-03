#----------------------------------------------------------------
#
# Used Cars
#
# Here we develop a complete "IT System" that combines a database
# back end with a GUI front end.  It provides a convenient way
# for users to search for used cars within a particular price
# range and of a particular make.
#
# NB: Before you can run this demo you need to create the
# "car_details" table by importing and running the
# "car_details.sql" script in the phpMyAdmin interface.
# You also need to insert your own database credentials in
# the call to the "connect" function below.
#
#
# Examples
#
# 1) Searching for a HOLDEN between $1000 and $3000 produces:
#    
#    16935: KINGSWOOD, $2924
#    16934: KINGSWOOD, $2476
#    16930: KINGSWOOD, $2045
#    17795: TORANA, $2895
#    17792: TORANA, $2538
#
# 2) Searching for a FORD between $2000 and $12000 produces:
# 
#    16107: CAPRI, $2950
#    16635: FAIRLANE, $4528
#    16767: FALCON, $3096
#    16477: CORTINA, $4919
#    16755: FALCON, $5790
#    16669: FAIRMONT, $8777
#    16587: ESCORT, $5840
#    16476: CORTINA, $6210
#    16718: FALCON, $8821
#    16475: CORTINA, $11411
#    16743: FALCON, $9780
#    17129: LASER, $8710
#    17104: LASER, $8056
#    16750: FALCON, $11672
#    17140: LASER, $7315
#    17744: TELSTAR, $10853
#    17139: LASER, $8636
#    17151: LASER, $10188
#    17106: LASER, $10983
#    17116: LASER, $9352
#
# 3) Searching for a VOLKSWAGEN between $1000 and $1500
#    produces nothing.  (The cheapest is $2059.)
#


#----------------------------------------------------------------

# Import the Tkinter functions
from Tkinter import *

# Import the MySQL-Python connector functions
from mysql.connector import *

# Alternative MySQL-Python connector
# from MySQLdb import *


#----------------------------------------------------------------
#
# The back end function which interrogates the database.  (We
# bind this function to a keyboard character below which obliges
# us to have an "event" parameter, which can be used to access
# the widget that called this function, however we don't use this
# capability here.)
#
def get_cars(event = None):
    # Get the user's preferences
    pref_make = make.get()
    minimum = min_price.get()
    maximum = max_price.get()
    # Connect to the "car reviews" database (put your login credentials here!)
    connection = connect(host='131.181.70.168',
                         user='9876543',
                         database='9876543',
                         password='???')
    cars_db = connection.cursor()
    # Create the SQL query
    query = """SELECT carId, model, price FROM car_details
               WHERE """ + minimum + """ <= price AND
               price <= """ + maximum + """ AND
               make = '""" + pref_make + """'"""
    # Execute the query
    cars_db.execute(query)
    # Display the results in the text area
    results_text.delete(0.0, END)
    for row in cars_db.fetchall():
        car_details = row[0] + ': ' + row[1] + ', $' + str(row[2]) + '\n'
        results_text.insert(END, car_details)
    # Unlock the database
    cars_db.close()
    connection.close()


#----------------------------------------------------------------
#
# The front end main program which creates the GUI.
#
# Create a window
used_cars = Tk()

# Give the window a title
used_cars.title('Used Car Search')

# Create the "used car sale" image
sale_image = PhotoImage(file = 'used_cars.gif')
Label(used_cars, image = sale_image).\
                 grid(row = 0, column = 0, rowspan = 5)

# Create a text field to display the results (NB: On a Mac this
# text box allows vertical scrolling with the mouse wheel by
# default)
results_text = Text(used_cars, width = 24, height = 8,
                    wrap = WORD, bg = 'light grey', font = ('Arial', 16),
                    borderwidth = 2, relief = 'groove',
                    takefocus = False)
results_text.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

# Create labels for the three text entry fields
Label(used_cars, text = 'Minimum price:').\
    grid(row = 1, column = 1, sticky = E)

Label(used_cars, text = 'Maximum price:').\
    grid(row = 2, column = 1, sticky = E)

Label(used_cars, text = 'Preferred make:').\
    grid(row = 3, column = 1, sticky = E)

# Create a text entry field for the minimum price, with the
# text in the box preselected for replacement whenever the text
# entry field is made the "focus", and with this field being
# the initial focus when the window is first selected
min_price = Entry(used_cars, font = ('Courier', 16), justify = RIGHT, width = 10)
min_price.grid(row = 1, column = 2, sticky = W)
min_price.selection_range(0, END)
min_price.focus()

# Create a text entry field for the maximum price, with
# the text in the field preselected for replacement
max_price = Entry(used_cars, font = ('Courier', 16), justify = RIGHT, width = 10)
max_price.grid(row = 2, column = 2, sticky = W)
max_price.selection_range(0, END)

# Create a text entry field for the preferred make, with
# the text in the field preselected for replacement
make = Entry(used_cars, font = ('Courier', 16), justify = RIGHT, width = 10)
make.grid(row = 3, column = 2, sticky = W)
make.selection_range(0, END)

# Create a button to start the search
Button(used_cars, text = 'Search', takefocus = False, command = get_cars).\
    grid(row = 4, column = 1, columnspan = 2, pady = 5)

# Allow users to start the search by typing a carriage return
used_cars.bind('<Return>', get_cars)

# Start the event loop
used_cars.mainloop()
