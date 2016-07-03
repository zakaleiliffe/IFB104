#---------------------------------------------------------
#
# Count divisors
#
# A "divisor" of a natural number is a number less than or equal
# to the integer that divides the number without a remainder.
# For instance, 4 is a divisor of 12 because 12 / 4 = 3
# with nothing left over, but 7 is not a divisor of 12
# because 12 / 7 = 1 with 5 left over.
#
# Define a function to count the divisors of a given
# natural number and display the result in the form:
#
#     "x has y divisors"
# or
#     "x has one divisor"
#
# as appropriate, where x is the given number, and y is
# the number of divisors that x has.
#
# (Observation: Every number N has itself and 1 as
# divisors.)
#
# Hints:
#
# * Given a numerator n and and a denominator d, then
#   "n % d" returns the remainder after integer
#   division in Python.  If this value is 0 then
#   d must be a divisor of n.
#
# * This problem can be solve using a FOR loop, a
#   WHILE loop or recursion, but is probably easiest
#   using a FOR loop.

 
#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> count_divisors(10) # Test 1 (normal case)
10 has 4 divisors

>>> count_divisors(4) # Test 2 (normal case)
4 has 3 divisors

>>> count_divisors(24) # Test 3 (normal case)
24 has 8 divisors

>>> count_divisors(100) # Test 4 (normal case)
100 has 9 divisors

>>> count_divisors(1) # Test 5 (boundary case)
1 has one divisor

>>> count_divisors(7) # Test 6 (prime number)
7 has 2 divisors

"""


#---------------------------------------------------------
#

##### DEVELOP YOUR count_divisors FUNCTION HERE


# A procedure to count the divisors of a given non-negative number
# and display the result
#
def count_divisors(dividend):

    # Initialise a new integer variable to count divisors
    divisor_count = 0

    # Calculate how many divisors in the given number
    trial_divisors = range(1, dividend + 1)
    for divisor in trial_divisors:
        if dividend % divisor == 0:
            divisor_count = divisor_count + 1

    # Print an appropriate message
    if divisor_count == 1:
        print dividend, 'has one divisor'
    else:
        print dividend, 'has', divisor_count, 'divisors'


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
