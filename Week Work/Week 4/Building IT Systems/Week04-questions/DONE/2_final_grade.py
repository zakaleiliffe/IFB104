#---------------------------------------------------------
#
# Final grades
#
# QUT's default percentage cut-offs for the final grade
# awarded in a unit are as follows.
#
#  Percentage   Grade
#   0 .. 24       1
#  25 .. 39       2
#  40 .. 49       3
#  50 .. 64       4
#  65 .. 74       5
#  75 .. 84       6
#  85 .. 100      7
#
# Notice that this is not a simple linear relationship.
# The first grade covers 25 percentage marks, the
# second 15, the third 10, and so on.  Therefore, to
# write some code to translate percentage marks into
# grades we will need to use one or more conditional
# statements.
#
# Below are some unit tests for a function called
# "final_grade" which accepts a percentage as its sole
# parameter and returns the corresponding grade.  Your
# job is to write the function which passes all these
# tests.  Note in the final two tests that if an
# invalid percentage is provided then the function
# returns -1, which cannot be a valid result, to flag
# the error.
#
# Footnote: Although the ranges above are the default
# cut-offs, there is no guarantee they will used by a
# particular unit in a particular semester.  A School
# can always choose to change the cut-offs at the end
# of the semester.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> final_grade(85) # Test 1. Normal case - high distinction, borderline
7

>>> final_grade(80) # Test 2. Normal case - distinction
6

>>> final_grade(74) # Test 3. Normal case - borderline credit
5

>>> final_grade(49.9) # Test 4. Normal case - borderline pass, floating point
3

>>> final_grade(48) # Test 5. Normal case - just failed
3

>>> final_grade(25) # Test 6. Normal case - fail
2

>>> final_grade(10) # Test 7. Normal case - low fail
1

>>> final_grade(0) # Test 8. Boundary case - a very bad student
1

>>> final_grade(-1) # Test 9. Invalid case - mark too low
-1

>>> final_grade(110) # Test 10. Invalid case - mark too high
-1

"""

#---------------------------------------------------------
# A function which, when given a percentage, returns
# the corresponding grade.
#

##### DEFINE YOUR final_grade FUNCTION HERE

def final_grade(percentage):
    if percentage <= 24 and percentage >= 0:
        return 1
        
    elif percentage >= 25 and percentage < 40:
        return 2
        
    elif percentage >= 40 and percentage < 50:
        return 3
        
    elif percentage >= 50 and percentage < 65:
        return 4
        
    elif percentage >= 65 and percentage < 75:
        return 5
        
    elif percentage >= 75 and percentage < 85:
        return 6
        
    elif percentage >= 85 and percentage <= 100:
        return 7
        
    else:
        return -1
        
    
    
        


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)

