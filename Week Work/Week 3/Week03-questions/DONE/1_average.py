#---------------------------------------------------------
#
# Average
#
# As a very simple exercise in defining your own reusable
# function, define a function with two parameters, both numbers,
# that calculates and returns the average of those numbers.
#
# The tests below tell us how your function is expected to
# behave when called.  The main program of this file runs
# the tests, so after you've developed your function you
# can just "run" this file to see if you've succeeded.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> average(2, 10) # Test 1 - normal case
6.0

>>> average(3, 10) # Test 2 - fractional result
6.5

>>> average(9.5, 10) # Test 3 - floating point input
9.75

>>> average(5, 5) # Test 4 - same values
5.0

>>> average(0, 0) # Test 5 - boundary case
0.0

"""


#---------------------------------------------------------
# Problem solving strategy for the "average" function:
# 1. Return ...
# 2.  the sum of the two numbers ...
# 3.  divided by two.

#### PUT YOUR average FUNCTION DEFINITION HERE

def average(firstnumber, secondnumber):
    firstnumber = float(firstnumber)
    answer =(firstnumber + secondnumber) / 2
    return float(answer)


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

