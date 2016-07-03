#---------------------------------------------------------
#
# Weather Warning
#
# Define a function which accepts one argument, a number
# representing a temperature in Celsius.
# The function should print warnings about extreme
# temperatures.
#
# Warnings should be issued for temperatures as follows:
#   above 40          = 'Extreme heat caution!'
#   between 30 and 40 = 'Warm weather'
#   between 10 and 20 = 'Cool weather'
#   below 10          = 'Extreme cold caution!'
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> weather_warning(31) # Test 1. Normal case
Warm weather

>>> weather_warning(27) # Test 2. Normal case - no warning issued

>>> weather_warning(38) # Test 3. Normal case
Warm weather

>>> weather_warning(0) # Test 4. Normal case
Extreme cold caution!

>>> weather_warning(100) # Test 5. Normal case
Extreme heat caution!

>>> weather_warning(10) # Test 6. Normal case
Cool weather

>>> weather_warning(-34) # Test 7. Normal case - negative number
Extreme cold caution!

>>> weather_warning(9) # Test 8. Boundary case
Extreme cold caution!

>>> weather_warning(24) # Test 9. Normal case - no warning issued

"""


#---------------------------------------------------------
# Define a function to issue warnings about the weather
# given a temperature in Celsius, as per the tests
# above.

##### DEFINE YOUR weather_warning FUNCTION HERE
        

#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
