#----------------------------------------------------------------
#
# Line numbering
#
# Define a function which accepts one argument, the name of a
# text file and prints the contents of that file line by line.
# Each line must be preceded by the line number.  For instance,
# the file 'joke.txt' will be printed as follows:
#
# 1 A Joke
# 2 
# 3 One spring morning - so the story goes - two village tradesmen
# 4 met on the road to work.  Said one, noticing that his mate's
# 5 ...
#
# (It appears that our sense of humour has changed a bit in the
# last century!)
#
# Optional: Since the number of digits in the line number changes,
# you can make the output look neater by using Python's "rjust"
# function, or similar, to produce the line numbers in a fixed
# number of spaces.
#
# Note: You should open the file in "Universal mode" so that
# it doesn't matter whether the text lines are terminated with
# Microsoft DOS, Apple or UNIX/Linux newline characters.
#
# Note: When you read a line of text from a file it will have a
# "newline" character at the end.  Since Python's "print"
# command usually produces a newline at the end of its output
# this will result in extra blank lines being written.  There are
# two ways to solve this:
#
# 1) Remove the newline character '\n' from the end of each line
#    before printing; or
# 2) Put a comma at the end of the "print" statement, which tells
#    it to print without writing a newline.
#


#----------------------------------------------------------------
#

#### DEVELOP YOUR print_line_numbers FUNCTION HERE



text_in = open('joke.txt', 'U')
number = 0

for line in text_in:
    print (number + 1) , line,

text_in.close()

        
        


#----------------------------------------------------------------
#
# Some tests - uncomment as needed.
#
#print_line_numbers('joke.txt')
# print_line_numbers('AnimalFarm-Chapter1.txt')
