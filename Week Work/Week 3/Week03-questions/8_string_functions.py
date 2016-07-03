##---------------------------------------------------------
##
##  A String Module
##
##  So far we have been defining individual functions.  In
##  this exercise you will create a module containing three
##  distinct functions for manipulating text strings.  This
##  module will then be used in the subsequent "Telegrams"
##  exercise.
##
##  The main program of this file has been constructed so
##  that it will NOT run the tests if this file is
##  imported into another program.
##
##  Hint: You will find some very helpful string methods for
##  this exercise in Section 5.6.1 of the Python Library
##  Reference manual.
##


#---------------------------------------------------------
# These are the tests your three functions must pass.  We
# have included a number of tests for each function.
#
""" 
Part 1: Tests for the convert_to_upper function

>>> convert_to_upper('what') # Test A1 - normal case (all lower case chars)
'WHAT'

>>> convert_to_upper('WHY') # Test A2 - normal case (all upper case chars)
'WHY'

>>> convert_to_upper('Which, Who, When') # Test A3 - normal case (mixed case chars)
'WHICH, WHO, WHEN'

>>> convert_to_upper('') # Test A4 - boundary case (empty string)
''


Part 2: Tests for the remove_spaces function

>>> remove_spaces('H E L P !!') # Test B1 - normal case (multiple spaces)
'HELP!!'

>>> remove_spaces('  The End   ') # Test B2 - normal case (leading and trailing spaces)
'TheEnd'

>>> remove_spaces('ThisOneIsOkAsIs') # Test B3 - boundary case (no spaces)
'ThisOneIsOkAsIs'

>>> remove_spaces('') # Test B4 - boundary case (empty string)
''

>>> remove_spaces('    ') # Test B5 - boundary case (only spaces)
''


Part 3: Tests for the replace_stops function

>>> replace_stops('Stop.') # Test C1 - normal case (one occurrence)
'StopSTOP'

>>> replace_stops('Need help. Reply urgently.') # Test C2 - normal case (two occurrences)
'Need helpSTOP Reply urgentlySTOP'

>>> replace_stops('...') # Test C3 - unusual case (nothing but full stops)
'STOPSTOPSTOP'

>>> replace_stops('Hello world, how are you today?') # Test C4 - boundary case (no full stops)
'Hello world, how are you today?'

"""


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all alphabetic characters in upper case.
# (Hint: This can be done trivially using Python's
# built-in "upper" method for strings.)

#### DEFINE YOUR convert_to_upper FUNCTION HERE


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all blank spaces removed.
# (Hint: This can be done easily using Python's built-in
# "replace" function for strings.)

#### DEFINE YOUR remove_spaces FUNCTION HERE


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all occurrences of full stops '.'
# replaced with the word 'STOP'.

#### DEFINE YOUR replace_stops FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above only if
# this file is "run" rather than "imported".
#
if __name__ == "__main__":
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE)
