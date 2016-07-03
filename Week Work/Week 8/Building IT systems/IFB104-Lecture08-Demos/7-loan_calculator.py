#-----------------------------------------------------------------
#
# Loan Calculator
#
# A GUI that provides an interface to functions for computing
# loan payments using compounding monthly interest.  (Inspired
# by an example in Y. Liang, "Introduction to Programming Using
# Python".)
#
# Example:
# Rate = 4.5%, Num years = 4, Loan amount = $5000
# Monthly payment = $114.02, Total payment = $5472.96
#

# Import the Tkinter functions
from Tkinter import *


# Two back-end functions that perform the financial calculations
#
def calculate_monthly_payment(rate, years, amount):
    return round(amount * (rate / 1200.0) /
                 (1 - (1 / (1 + (rate / 1200.0)) ** (years * 12))), 2)

def calculate_total_payment(monthly, years):
    return round(monthly * 12 * years, 2)


# When the button is pushed this function gets the user's inputs,
# does the calculation and diplays the results - it connects the
# front end to the back end.  (Below we bind this function to
# the carriage-return key on the keyboard which obliges
# us to have a dummy "event" parameter.)
#
def compute_payment(event = None):
    
    global monthly_result, total_result
    
    # Convert user's inputs to floats
    rate = float(interest_rate.get())
    years = float(num_years.get())
    amount = float(loan_amount.get())
    # Use the two back-end functions to do the calculation
    monthly_payment = calculate_monthly_payment(rate, years, amount)
    total_payment = calculate_total_payment(monthly_payment, years)
    # Display the results
    monthly_result['text'] = str(monthly_payment)
    total_result['text'] = str(total_payment)


# The front-end GUI program
# Create a window
loan_window = Tk()

# Give the window a title
loan_window.title('Loan Calculator')

# Create some fixed labels and arrange them in the main
# window
Label(loan_window, text = 'Annual interest rate:').\
                   grid(row = 1, column = 1, sticky = E)
Label(loan_window, text = 'Number of years:').\
                   grid(row = 2, column = 1, sticky = E)
Label(loan_window, text = 'Loan amount:').\
                   grid(row = 3, column = 1, sticky = E)
Label(loan_window, text ='Monthly payment:').\
                   grid(row = 4, column = 1, sticky = E)
Label(loan_window, text ='Total payment:').\
                   grid(row = 5, column = 1, sticky = E)

# Create three text entry fields and arrange them in the
# main window
interest_rate = Entry(loan_window, width = 10, justify = RIGHT)
num_years = Entry(loan_window, width = 10, justify = RIGHT)
loan_amount = Entry(loan_window, width = 10, justify = RIGHT)
interest_rate.grid(row = 1, column = 2)
num_years.grid(row = 2, column = 2)
loan_amount.grid(row = 3, column = 2)

# Make the first text entry field the initial focus for
# user inputs when the main window is selected
interest_rate.focus()

# Create two labels in the main window which will be used
# to display the results
monthly_result = Label(loan_window, text = '--.--')
total_result = Label(loan_window, text = '--.--')
monthly_result.grid(row = 4, column = 2, sticky = E)
total_result.grid(row = 5, column = 2, sticky = E)

# Create a button which starts the calculation when pressed
Button(loan_window, text = 'Calculate', command = compute_payment,
       takefocus = False).grid(row = 6, column = 2, sticky = E)

# As well as pressing the button, allow users to start the
# calculation by typing a carriage return on the keyboard
loan_window.bind('<Return>', compute_payment)

# Start the event loop
loan_window.mainloop()
