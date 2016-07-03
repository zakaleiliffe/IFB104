#---------------------------------------------------------
#
# Is the number a square?
#
# Define a Boolean function with one parameter, a number,
# which determines if that number is a square of an integer.
# A Boolean function is one which returns True or False
# - also called a 'predicate'.
#
# Hints: A given number is the square of an integer if
# its square root is a whole number.  A whole number is
# one which has no remainder when divided by 1.
#
# Warning: Remember that negative numbers don't have a
# square root!
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> square(9) # Test 1. Normal case
True

>>> square(100) # Test 2. Normal case
True

>>> square(99) # Test 3. Normal case
False

>>> square(22500) # Test 4. Normal case
True

>>> square(134688) # Test 5. Normal case
False

>>> square(1) # Test 6. Boundary case
True

>>> square(0) # Test 7. Boundary case
True

>>> square(-1) # Test 8. Boundary case
False

>>> square(-100) # Test 9. Normal case
False

"""


#---------------------------------------------------------

##### DEFINE YOUR square FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

