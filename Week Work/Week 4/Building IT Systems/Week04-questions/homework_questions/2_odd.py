#---------------------------------------------------------
#
# Odd?
#
# Define a "predicate" function (one that returns True or False)
# with one parameter, an integer, that determines whether or
# not the given integer is odd.
#
# Hints: An odd integer is one which has something left over
# when it is divided by 2.  Python's built-in "n % d" operator
# returns the remainder when numerator n is divided by
# denominator d.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> odd(1) # Test 1. Normal case
True

>>> odd(4) # Test 2. Normal case
False

>>> odd(1000001) # Test 3. Normal case
True

>>> odd(0) # Test 4. Boundary case
False

>>> odd(-1) # Test 5. Another boundary case
True

"""


#---------------------------------------------------------

##### DEFINE YOUR odd FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

