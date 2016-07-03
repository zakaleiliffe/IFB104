#---------------------------------------------------------------------
#
# Demonstration - Printing versus returning values
#
# The small examples in this file illustrate the difference between
# printing a value from within a function and having the function
# return a value.
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
# The following function RETURNS the obscured number
#

# Return an obscured version of a given secret such as a
# credit card or bank account number
#
def obscure(secret):
    first_position = 0
    last_position = len(secret) - 1
    asterisks = '*' * (len(secret) - 2)
    return secret[first_position] + asterisks + secret[last_position]

print 'Card 5685 8675 2411 9076 obscured is',
print obscure('5685 8675 2411 9076') # show the returned value

print 'The type of the returned value is:',
print type(obscure('5685 8675 2411 9076')) # show its type

print

#---------------------------------------------------------------------
#
# The following procedure PRINTS, but does not return, the obscured
# credit card number
#

# Print an obscured version of a credit card or bank card
# number
#
def show_obscured_number(secret): 
    first_position = 0
    last_position = len(secret) - 1
    asterisks = '*' * (len(secret) - 2)
    print secret[first_position] + asterisks + secret[last_position]

print 'Card 5685 8675 2411 9076 obscured is',
show_obscured_number('5685 8675 2411 9076')  # no need to "print" this expression

print 'The type returned by the second function is:',
print type(show_obscured_number('5685 8675 2411 9076')) # notice the annoying side effect
                                                        # when this line is "run"!
