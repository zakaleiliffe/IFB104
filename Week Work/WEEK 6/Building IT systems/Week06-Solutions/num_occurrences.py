#----------------------------------------------------------------
#
# Number of occurrences of a phrase in a file
#
# Define a function which accepts two string-valued arguments,
# the name of a text file and a string representing a particular
# phrase we expect to occur in the file.  The function must
# return the number of occurrences of that phrase in the file.
#
# NB: The capitalisation of the phrase shouldn't matter.
#
# NB: Keep in mind that the phrase may appear more than once
# on a given line.
#
# Observation: If the phrase is a long one containing multiple
# words it may be split across two or more lines.  For the
# purposes of this exercise we will not attempt to find such
# occurrences, only those where the phrase appears wholly within
# one line.
#


#----------------------------------------------------------------
#
# Some tests
#
"""
>>> num_occurrences('joke.txt', 'one') # Test 1
2

>>> num_occurrences('AnimalFarm-Chapter1.txt', 'Mr. Jones') # Test 2
4

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Mr. Jones') # Test 3
23

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Comrades') # Test 4
56

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Internet') # Test 5
0
"""


#----------------------------------------------------------------
#
# A solution
#

# Count the number of times a particular phrase appears in
# a text file
#
def num_occurrences(filename, phrase):

    # Open the file
    the_file = open(filename, 'U')

    # Initialise the occurrence counter
    how_many = 0

    # Remove case sensitivity from the phrase
    lower_phrase = phrase.lower()

    # Check how many times the phrase appears in each line
    # each line of the file 
    for line in the_file:
        # Remove case sensitivity from the line
        lower_line = line.lower()
        # Add the number of occurrences on this line to the counter
        how_many = how_many + lower_line.count(lower_phrase)

    # Close the file
    the_file.close()

    # Return the total
    return how_many


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
