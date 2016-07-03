#-----------------------------------------------------------------
#
# Robust Loan Calculator
#
# The following GUI program was previously used as a lecture
# demonstration.  When the user enters three numbers it
# calculates the monthly payment and total payment on a
# bank loan.
#
# Example:
# Rate = 4.5%, Num years = 4, Loan amount = $5000
# Monthly payment = $114.02, Total payment = $5472.96
#
# However, the program does not work properly if the user
# does not enter valid numbers into the text entry boxes,
# typically producing red error messages in IDLE's shell
# window, indicating unhandled exceptions.
#
# Extend the program below with exception handling code
# so that it responds appropriately to invalid user inputs.
# Note that when the program starts up the "payment" labels
# are set to default values '--.--' indicating that there
# is nothing to display.  Therefore, a good strategy is to
# display these strings whenever the user enters invalid
# inputs to show that no valid results can be calculated.
#

# Import the Tkinter functions
from Tkinter import *


# Two back-end functions that perform the financial calculations
def calculate_monthly_payment(rate, years, amount):
    return round(amount * (rate / 1200.0) /
                 (1 - (1 / (1 + (rate / 1200.0)) ** (years * 12))), 2)

def calculate_total_payment(monthly, years):
    return round(monthly * 12 * years, 2)


# When the button is pushed this function gets the user's inputs,
# does the calculation and diplays the results; it connects the
# front end to the back end
def compute_payment():
    global monthly_result, total_result

    # Convert user's inputs to floats
    rate = float(interest_rate.get())
    years = float(num_years.get())
    amount = float(loan_amount.get())
    # Use the back-end functions to do the calculation
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
interest_rate = Entry(loan_window, justify = RIGHT)
num_years = Entry(loan_window, justify = RIGHT)
loan_amount = Entry(loan_window, justify = RIGHT)
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
Button(loan_window, text = 'Calculate', command = compute_payment).\
                    grid(row = 6, column = 2, sticky = E)

# Start the event loop
loan_window.mainloop()
