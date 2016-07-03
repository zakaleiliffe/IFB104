#---------------------------------------------------------------
#
# Quadchart
#
# A quadchart is a commonly-used decision making tool, applicable
# when a decision is based on two Boolean values.  In this
# exercise you will develop a function which makes a
# quadchart-based decision.
#
# Imagine that you need to decide what activity to perform today,
# based on two facts, whether or not the weather is nice and
# whether or not it's the weekend.  Your options could be
# presented as the following quadchart.
#
#                  Weather nice       Weather not nice
#                +------------------+------------------+
#                |                  |                  |
#  Weekend today | Go to the beach! | Catch a movie!   |
#                |                  |                  |
#                +------------------+------------------+
#                |                  |                  |
#  Weekday today | Daydream time    | Good day to work |
#                |                  |                  |
#                +------------------+------------------+
#
# Define a function which expects two Boolean arguments:
#   a value which is True if the weather is fine; and
#   a value which is True if it is the weekend.
# Depending on the weather and the day of the week, print
# an appropriate message according to the table above.
# 


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> today(True, True) # Test 1. Normal case
Go to the beach!

>>> today(True, False) # Test 2. Normal case
Daydream time

>>> today(False, True) # Test 3. Normal case
Catch a movie!

>>> today(False, False) # Test 4. Normal case
Good day to work

"""


#---------------------------------------------------------

##### DEFINE YOUR today FUNCTION HERE

def today(weather_fine, is_the_weekend):
    if weather_fine and is_the_weekend:
        print "Go to the beach!"
    if not weather_fine and is_the_weekend:
        print "Catch a movie!"
    if weather_fine and not is_the_weekend:
        print "Daydream time"
    if not weather_fine and not is_the_weekend:
        print "Good day to work"


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
