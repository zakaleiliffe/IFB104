#---------------------------------------------------------
#
# Find first negative
#
# Define a function with one parameter, a list of numbers.
# The function should return the first negative number in
# that list, or return 0 if there are no negative
# numbers.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
Normal case - different numbers
>>> first_negative([1, 2, 3, -4, 5, 6]) # Test 1
-4

Normal case - all the same negative number
>>> first_negative([-2, -2,- 2, -2]) # Test 2
-2

Normal case - some duplicates
>>> first_negative([3, -14, 1, -20, 3, -14, -20, 6]) # Test 3
-14

Normal case - no negatives
>>> first_negative([4, 1, 2, 3, 4, 2, 6]) # Test 4
0

Normal case - all negatives
>>> first_negative([-3, -1, -2, -3, -4, -2, -6]) # Test 5
-3

Normal case - check for returned value, rather than printed
>>> first_negative([7, -3, -4, 5]) == -3 # Test 6
True

"""


#---------------------------------------------------------
#

##### DEVELOP YOUR first_negative FUNCTION HERE

# A function to find the first negative number
# in a list (or return 0 if there are none)
#
def first_negative(numbers):

    # Check each number
    for value in numbers:
        if value < 0:
            return value # Exit loop early

    # No negative numbers found
    return 0 


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
