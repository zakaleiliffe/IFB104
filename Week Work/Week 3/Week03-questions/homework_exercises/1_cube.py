##---------------------------------------------------------
##
##  Cube
##
##  As a very easy exercise in defining your own reusable
##  code, define a function with one parameter, a number,
##  that returns the cube of that number.
##
##  A cube is a number multiplied by itself three times, or
##  in other words, to the power of 3
##  e.g., 4 cubed = 4 x 4 x 4 = 64.
##
##  The tests below tell us how your function is expected to
##  behave when called.  The main program of this file runs
##  the tests, so after you've developed your function you
##  can just "run" this file to see if you've succeeded.



#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> cube(2) # Test 1 - normal case
8

>>> cube(10) # Test 2 - normal case
1000

>>> cube(.5) # Test 3 - floating point
0.125

>>> cube(1) # Test 4 - boundary case 
1

>>> cube(0) # Test 5 - boundary case 
0

"""


#---------------------------------------------------------
# Your solution
#

#### DEFINE YOUR cube FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
