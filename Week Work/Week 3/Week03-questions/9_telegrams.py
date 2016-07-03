##---------------------------------------------------------
##
##  Telegrams
##
##  Define a function with one parameter, a string representing
##  a message.  Your function is to return that message in capital
##  letters, with every full-stop replaced with "STOP", and 
##  all spaces removed, so that it looks like an old-fashioned
##  telegram.  (Telegrams were sent on equipment that could transmit
##  upper-case letters only.  The operator would cut the words
##  from a ticker-tape strip and paste them onto a piece of paper
##  to create the telegram for delivery to the recipient.)
##
##  As an exercise in reuse of functions, you must do this using
##  your solution to the "string_functions" exercise.  Import and
##  use your previously defined functions "replace_stops",
##  "remove_spaces" and "convert_to_upper".


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> telegram('URGENTMESSAGEPLEASEREAD') # Test 1 - all caps, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram('UrgentMessagePleaseRead') # Test 2 - mixed case, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram('Urgent Message.  Please Read.') # Test 3 - normal case
'URGENTMESSAGESTOPPLEASEREADSTOP'

>>> telegram("Do not stop.") # Test 4 - normal case
'DONOTSTOPSTOP'

>>> telegram(' . . . ') # Test 5 - unusual case: only stops and spaces
'STOPSTOPSTOP'

>>> telegram('') # Test 6 - boundary case: empty string 
''

"""


#---------------------------------------------------------
# Import your solutions from the "string_functions"
# exercise.  Remember to remove the "difficulty level"
# prefix from the Python file name (or add it below).
#
from string_functions import *


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it in telegram format, i.e., all in caps, with full-stops
# replaced with the word "STOP" and spaces removed.
#

#### DEFINE YOUR telegram FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
