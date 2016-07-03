##---------------------------------------------------------
##
##  Temperature Conversion
##
##  Define a function with one parameter, a number representing
##  a temperature in Fahrenheit, that returns that temperature
##  in Celsius.  In general the relationship between a temperature
##  in Celsius C and the corresponding temperature in Fahrenheit F
##  is C = (F - 32) * (5 / 9).
##
##  The tests below tell us how your function is expected to
##  behave when called.  The main program of this file runs
##  the tests, so after you've developed your function you
##  can just "run" this file to see if you've succeeded.
##
##  NB: Some of the tests below depend on the precision of arithmetic
##  on your computer.  Therefore we have used the "round" function
##  to round the answers off to whole numbers.


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> fahrenheit_to_celsius(32) # Test 1 - normal case (freezing point)
0.0

>>> fahrenheit_to_celsius(212) # Test 2 - normal case (boiling point)
100.0

>>> round(fahrenheit_to_celsius(100)) # Test 3 - normal case (hot day!)
38.0

>>> round(fahrenheit_to_celsius(70)) # Test 4 - normal case
21.0

>>> fahrenheit_to_celsius(86) # Test 5 - normal case 
30.0

>>> fahrenheit_to_celsius(-40) # Test 6 - special case (same result)
-40.0

>>> fahrenheit_to_celsius(32) == 0.0 # Test 7 - check value returned not printed
True

"""


#---------------------------------------------------------
# Your solution
#

#### DEFINE YOUR fahrenheit_to_celsius FUNCTION HERE
def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = float(fahrenheit)
    answer = (fahrenheit - 32) * (float(5) / 9)
    return answer


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

