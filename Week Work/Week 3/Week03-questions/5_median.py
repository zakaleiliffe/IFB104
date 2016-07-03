##---------------------------------------------------------
##
##  Median
##
##  The median of a set of values is a measure of central
##  tendency like the average, but has the advantage of
##  being less affected by outliers.  Define a function
##  with one parameter, a non-empty list, which returns
##  the median item in that list.
##
##  For the purpose of this exercise, the median item is
##  the middle value (or the second of two middle values)
##  when the list is arranged in ascending order.
##
##  (In fact, the mathematical median is the middle value
##  when the given list has an odd length, but is the
##  average of the two values in the middle when the list
##  contains an even number of items.  We ignore this
##  fine distinction here.)
##
##  The tests below tell us how your function is expected to
##  behave when called.  The main program of this file runs
##  the tests, so after you've developed your function you
##  can just "run" this file to see if you've succeeded.
 

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> median([8, 5, 1, 2, 3]) # Test 1 - normal case (list of numbers)
3

>>> median([-5, -6, -10, -8, -7, -8, -1]) # Test 2 - normal case (negatives)
-7

>>> median([1, 1, 1, 1, 1, 1, 1, 1, 1]) # Test 3 - normal case (same numbers)
1

>>> median([0, 1, 67899, 2, 100000, 5, 4, -54321, 3]) # Test 4 - normal case (small and large numbers)
3

>>> median(['Donna', 'Kim', 'Alice', 'Joe']) # Test 5 - normal case (list of strings)
'Joe'

>>> median([99]) # Test 6 - boundary case (list of length one)
99

"""


#---------------------------------------------------------
# Solution strategy:
# 1. Sort the given list
# 2. Calculate the position of the middle value
# 3. Return the value at that position
#

#### DEFINE YOUR median FUNCTION HERE

###Calculating position of the middle value

listofvalues = [median]
sorted(listofvalues)
amountofvalues = (len(listofvalues))
middlenumber = amountofvalues / 2




##listofnumbers.append(somenumber)
##listofnumbers.append(len.allnumbersinlist)

#def median(numbers):
    

   # somenumbers = [somenumbers]
   # amount_of_numbers = int(len(somenumbers))








    
    


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
#from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
#print testmod(verbose = False,
             # optionflags = REPORT_ONLY_FIRST_FAILURE)
