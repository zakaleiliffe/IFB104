######################################################################
##
##  Demonstration - Locate negatives
##
##  The following function contains two coding errors.  Although it
##  sometimes produces the right answer, it doesn't always do so.
##  The aim of this demonstration is to use IDLE's debugger (and/or
##  PRINT statements) to help pinpoint the errors.  (The corrected
##  code is given in the comment at the end of this file.)
##


#---------------------------------------------------------------------
#
# The requirement:
#
# Given a list of integers, define a function that returns the
# positions (indices) of all negative numbers in the list.
#


#---------------------------------------------------------------------
#
# A faulty implementation:
#
# The following attempted solution to the above requirement contains
# (at least) two coding errors.  Can you identify them using the
# debugger?
#

# Return the positions of the negative numbers in a list
def locate_negatives(numbers):

    locations = []
    location = 0

    while location < len(numbers) - 1:
        location = location + 1
        if not (numbers[location] > 0):
            locations = locations + [location]
            
    return locations


# A test containing three negative numbers to locate:
print locate_negatives([-1, 9, -8, 3, 0, -5, 8])







































##---------------------------------------------------------------------
##
##    The two bugs in the program are:
##
##        1) The WHILE loop is incorrectly coded so that it never examines
##           the first item (at position zero).
##
##        2) The condition in the IF statement is incorrectly written so
##           that it adds zeros to the "locations" list as well as
##           negative numbers.
##
##    A corrected version of the function is as follows:
##        
##    def locate_negatives(numbers):
##
##        locations = []
##        location = 0
##
##        while location < len(numbers):
##            if numbers[location] < 0:
##                locations = locations + [location]
##            location = location + 1
##            
##        return locations
