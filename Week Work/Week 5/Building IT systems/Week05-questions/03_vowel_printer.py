#---------------------------------------------------------
#
# Vowel printer
#
# Define a function with one parameter, a string,
# which prints each of vowels the string contains
# (including duplicates), one on each line.
#
# Recall that the vowels in english are a, e, i, o and u.
#

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> vowel_print('abc') # Test 1
a

>>> vowel_print('My very elegant mother just sat upon nine porcupines') # Test 2
e
e
e
a
o
e
u
a
u
o
i
e
o
u
i
e

>>> vowel_print('The quick brown fox jumps over the lazy dog') # Test 3
e
u
i
o
o
u
o
e
e
a
o

>>> vowel_print('aeiou') # Test 4
a
e
i
o
u

>>> vowel_print('') # Test 5 (prints nothing)

>>> vowel_print('xyzzy') # Test 6 (prints nothing)

"""


#---------------------------------------------------------
#

##### DEVELOP YOUR vowel_print FUNCTION HERE



#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)


