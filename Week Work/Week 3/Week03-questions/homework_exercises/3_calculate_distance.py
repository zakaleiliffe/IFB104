##---------------------------------------------------------
##
##  Calculate Distance
##
##  Define a function with two parameters, a number to
##  represent time taken (in minutes) and average speed
##  (in kms/hr).  The function should return the distance
##  travelled given the time taken and the average speed.
##
##  The tests below tell us how your function is expected to
##  behave when called.  The main program of this file runs
##  the tests, so after you've developed your function you
##  can just "run" this file to see if you've succeeded.
##
##  Comment: Notice in the third test case below that we
##  round the result to two decimal places.  This is because
##  the actual answer returned, i.e., 16.6666..., may depend
##  on the precision of your particular computer architecture.


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> calculate_distance(60, 1) # Test 1 - normal case
1.0

>>> calculate_distance(30, 1) # Test 2 - fractional result
0.5

>>> round(calculate_distance(1, 1000), 2) # Test 3 - high speed
16.67

>>> calculate_distance(60000, 1) # Test 4 - low speed
1000.0

>>> calculate_distance(600, 0) # Test 5 - boundary case, no speed 
0.0

>>> calculate_distance(60, 1) == 1.0 # Test 6 - check value is returned not printed
True

"""


#---------------------------------------------------------
# Solution strategy: You will need to calculate how far
# the vehicle travels in one minute and then multiply
# this by the time taken.
#

### PUT YOUR calculate_distance FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

