#----------------------------------------------------------------
#
# Suspect words
#
# The implications of widespread monitoring of electronic
# communications is a very topical issue.  One way this can
# be done is to look for certain words in phrases taken from
# (decrypted) text messages or (transcribed) phone calls.
#
# Define a function which expects a single string argument,
# and determines if any of the following three "suspect" words
#     'bomb', 'knife' or 'gun'
# appear anywhere in that string, regardless of their
# capitalisation.
#
# Hints: You will find some of the functions in Python's "string"
# module helpful.  Also note that the Boolean "in" operator can be
# used on strings too.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> suspect_words('Hello everybody!') # Test 1. Normal case - a safe string
False

>>> suspect_words('I have a knife in my hand') # Test 2. Normal case - a disturbing string
True

>>> suspect_words('Greetings from Bombay') # Test 3. Normal case - accidently contains a forbidden word
True

>>> suspect_words('We had begun to sing') # Test 4. Normal case - accidently contains a forbidden word
True

>>> suspect_words('Cut the bombalaska with a knife please!') # Test 5. Normal case - contains two forbidden words
True

>>> suspect_words('KnIfE') # Test 6. Normal case - forbidden word, mixed case
True

>>> suspect_words('Gunna have a good time tonight!') # Test 7. Normal case - forbidden word, mixed case
True

>>> suspect_words('Being unhelpful') # Test 8. Normal case - forbidden word 'gun' is broken by space
False

>>> suspect_words('Some non-violent phrase') # Test 9. Normal case - no forbidden words
False

>>> suspect_words('guNbombgunbOMbknifeBomB') # Test 10. Normal case - only forbidden words, no spaces
True

>>> suspect_words('') # Test 11. Boundary case - empty string
False

"""


#---------------------------------------------------------

##### DEFINE YOUR suspect_words FUNCTION HERE


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
