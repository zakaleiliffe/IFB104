#---------------------------------------------------------------------
#
# Demonstration - Automatically testing a function
#
# This file illustrates the way we can use Python's "doctest"
# module to automatically run several tests of a function.
#
# Scenario: As a security measure, credit card and ATM receipts
# usually print only part of the card number, with the other
# digits replaced by asterisks.  The goal here is to produce a
# function that obscures any given string by printing only
# the first and last characters, with asterisks replacing all
# other characters.
#


#---------------------------------------------------------------------
#
# The following triple-quoted string contains the various tests that
# we want applied to the function.  Note that they're written in
# exactly the same way they would appear if you ran each test
# manually in the shell window.  The first tests are "typical" ones,
# but these are followed by some more extreme tests.  (In the last
# case our strategy for obscuring text proves to be ineffective!)
#
'''

>>> obscure('private')
'p*****e'

>>> obscure('INVISIBLE')
'I*******E'

>>> obscure('0123456789')
'0********9'

>>> obscure('******')
'******'

>>> obscure('XYZ')
'X*Z'

>>> obscure('AB')
'AB'

'''


#---------------------------------------------------------------------
#
# This is the function we want to test.  It returns an obscured
# version of a given secret such as a credit card or bank account
# number.
#
def obscure(secret):
    first_position = 0
    last_position = len(secret) - 1
    asterisks = '*' * (len(secret) - 2)
    return secret[first_position] + asterisks + secret[last_position]


#---------------------------------------------------------------------
#
# This code automatically runs the unit tests, using the docstring
# defined above. See Section 25.2 of the "Python Library
# Reference" for further detail.  To avoid being overwhelmed with
# output, we've requested a non-verbose result and that only the
# first failure is described, if any.  Normally "testmod" prints
# nothing if all the tests succeed, which is a bit anticlimactic,
# so we've printed the value it returns, to allow us to see the
# outcome in all cases.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
