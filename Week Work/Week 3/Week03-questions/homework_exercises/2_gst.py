##---------------------------------------------------------
##
##  Goods and Services Tax
##
##  Define a function with one parameter, a number representing
##  a wholesale price, that returns the GST component to be added
##  to that wholesale price (where GST is 10%).
##
##  The tests below tell us how your function is expected to
##  behave when called.  The main program of this file runs
##  the tests, so after you've developed your function you
##  can just "run" this file to see if you've succeeded.
##
##  Observation: Computer-based floating point arithmetic doesn't always
##  produce mathematically-precise results (see Appendix B of the Python
##  Tutorial).  Therefore, we've rounded off the answers to two decimal
##  places in the tests.


#---------------------------------------------------------
# These are the tests your function must pass.
#
"""
>>> round(gst(100), 2) # Test 1 - normal case
10.0

>>> round(gst(123.56), 2) # Test 2 - normal case
12.36

>>> round(gst(100 + 50), 2) # Test 3 - wholesale price as an expression
15.0

>>> round(gst(0), 2) # Test 4 - boundary case (price is zero)
0.0

>>> round(gst(123456789), 2) # Test 5 - price is large number
12345678.9

"""


#---------------------------------------------------------
# Your solution
#

#### DEFINE YOUR gst FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

