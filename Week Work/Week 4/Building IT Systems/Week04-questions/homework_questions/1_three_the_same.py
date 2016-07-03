#---------------------------------------------------------
#
# Three the same
#
# Define a "predicate" function (one that returns True or False)
# with three parameters.  The function should return True
# only if all three parameters have the same value.
#
# Comment: This is very easy in Python compared to some older
# programming languages.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> same(1, 2, 3) # Test 1. Normal case
False

>>> same('b', 'b', 'b') # Test 2. Normal case, another type
True

>>> same('b', 'b', 'a') # Test 3. Normal case
False

>>> same([3], [3, 3], [3]) # Test 4. Normal case, yet another type
False

>>> same([], [], []) # Test 5. Normal case
True

"""


#---------------------------------------------------------

##### DEFINE YOUR same FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

