#---------------------------------------------------------
#
# Robust divider program
#
# The interactive function called "divider" below
# prompts the user for two numbers, a dividend and a
# divisor, and returns their quotient (i.e., the first
# value divided by the second).
#
# However, this function crashes if the user types something
# that isn't a number or enters 0 as the divisor.  Your job
# is to define a new function, called "robust_divider"
# which calls the "divider" function but catches the
# various exceptions it may raise and prints a meaningful
# message for each.  Importantly, *you may not change*
# the original "divider" function when developing your
# "robust_divider" function.
#
# NB: Since these functions depend on inputs entered by
# the user it is difficult to construct automated unit tests
# for them.  (This can be done, but is awkward.)  Instead,
# therefore, we have described typical test cases below
# as comments only.
#


##---------------------------------------------------------
##
##    TESTCASES
##
##    Some typical interactions where the user's inputs are all
##    valid, using the original, fragile divider function:
##
##    >>> divider()
##    Please enter the dividend: 8
##    Please enter the divisor: 2
##    4
##
##    >>> divider()
##    Please enter the dividend: -15
##    Please enter the divisor: 3
##    -5
##
##    >>> divider()
##    Please enter the dividend: 100.0
##    Please enter the divisor: 20 + 5
##    4.0
##
##    >>> divider()
##    Please enter the dividend: 10.0 - 3
##    Please enter the divisor: 8
##    0.875
##
##    The robust_divider function should provide exactly
##    the same behaviour when the user's inputs are valid:
##
##    >>> robust_divider()
##    Please enter the dividend: 20
##    Please enter the divisor: 4
##    5
##
##    >>> robust_divider()
##    Please enter the dividend: 10.0 - 3
##    Please enter the divisor: 7
##    1.0
##
##    But interactions where the user's inputs are invalid
##    will cause the divider function's calculation to
##    raise an exception which must be caught by the
##    robust_divider function:
##
##    >>> robust_divider()
##    Please enter the dividend: 45
##    Please enter the divisor: blob
##    Unknown value entered!
##
##    >>> robust_divider()
##    Please enter the dividend: 'a'
##    Please enter the divisor: 'b'
##    Non-numeric value entered!
##
##    >>> robust_divider()
##    Please enter the dividend: 15
##    Please enter the divisor: 0
##    Cannot divide by zero!
##
##---------------------------------------------------------



# A fragile function to prompt the user for two numbers
# and return their quotient
def divider():
    # Read the dividend and divisor
    dividend = input('Please enter the dividend: ')
    divisor = input('Please enter the divisor: ')
    # Return the quotient
    return dividend / divisor


### CREATE YOUR robust_divider FUNCTION BY EXTENDING
### THE CODE BELOW

# A robust function to call the divider function,
# catch any exceptions it may raise, and print
# error messages accordingly
def robust_divider():
    return divider()

