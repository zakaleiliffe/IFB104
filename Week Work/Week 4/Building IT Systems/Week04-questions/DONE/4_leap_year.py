#---------------------------------------------------------
#
# Leap Years
#
# Leap years are used to account for the fact that the
# astronomical year, the time it takes the Earth to orbit
# the Sun once, is not exactly synchronised with the
# standard calendar year of 365 days.  Roughly speaking
# we experience a leap year of 366 days every four years,
# but in fact the rules governing leap years are more
# complex than that.  To decide whether or not a given
# year is a leap year or not, we therefore need to use
# one or more conditional statements (or expressions).
#
# Below are some tests for a Boolean-valued function
# (or "predicate") which returns True if a given year
# is a leap year and False otherwise.  Your task is
# to write the function that does this.
#
# Normally a leap year is a year which is evenly
# divisible by 4.  However, if it is also divisible
# by 100, then it must also be divisible by 400 to
# be a leap year.
#
# For instance: 1700, 1800, 1900, 2100, 2200, 2300,
# 2500, 2600 are NOT leap years but 1600, 2000, 2400
# ARE leap years.
#
# Hint: A number X is evenly divisible by another number Y
# if X % Y == 0, i.e., if the remainder after division is
# zero.
#
# 

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 

>>> leap_year(2008) # Test 1. Normal case - leap year
True

>>> leap_year(2000) # Test 2. Normal case - leap year
True

>>> leap_year(1600) # Test 3. Normal case - leap year
True

>>> leap_year(2014) # Test 4. Normal case - not a leap year
False

>>> leap_year(1900) # Test 5. Special case - not a leap year, divisible by 4 and 100, but not 400
False

"""


#---------------------------------------------------------
# Define a Boolean function to return True if the given
# year is a leap year, False otherwise.

##### DEFINE YOUR leap_year FUNCTION HERE

#year must  / 4 evenly
#year must / 100 and 400 evenly

def leap_year(year):    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False




       
    
    

    
#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

