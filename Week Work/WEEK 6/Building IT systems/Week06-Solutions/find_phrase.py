#----------------------------------------------------------------
#
# Find a phrase in a file
#
# Define a function which accepts two string-valued arguments,
# the name of a text file and a string representing a particular
# phrase we expect to occur in the file.  The function must
# print each line in the file where the phrase appears, including
# the line number.
#
# NB: The capitalisation of the phrase shouldn't matter, so if
# we search for the phrase 'one' in joke.txt, both lines
#
#   One spring morning - so the story goes - two village tradesmen
#
# and
#
#   met on the road to work.  Said one, noticing that his mate's
#
# should be displayed.  Hint: You will find Python's "lower"
# function useful for doing this.
#
# Observation: If the phrase is a long one containing multiple
# words it may be split across two or more lines.  For the
# purposes of this exercise we will not attempt to find such
# occurrences, only those where the phrase appears wholly within
# one line.
#


#----------------------------------------------------------------
#
# A solution
#

# Print those lines in a given file containing a particular
# phrase
#
def find_phrase(filename, phrase):

    # Open the file
    the_file = open(filename, 'U')

    # Initialise the line counter
    line_num = 0

    # Print each line in the file that contains the
    # phrase
    for line in the_file:
        # Increment the line counter
        line_num = line_num + 1
        # Print the line if it contains the phrase
        if phrase.lower() in line.lower():
            print str(line_num).rjust(3), line, # don't add another newline

    # Close the file
    the_file.close()


#----------------------------------------------------------------
#
# Some tests - uncomment as needed.
#
find_phrase('joke.txt', 'one') # should produce 2 lines
# find_phrase('AnimalFarm-Chapter1.txt', 'Major') # should produce 11 lines
# find_phrase('AnimalFarm-Chapter1.txt', 'Old Major') # should produce 3 lines
# find_phrase('AnimalFarm-TheWholeBook.txt', 'Snowball!') # should produce 2 lines
# find_phrase('AnimalFarm-TheWholeBook.txt', 'wheat crop') # should produce 2 lines
