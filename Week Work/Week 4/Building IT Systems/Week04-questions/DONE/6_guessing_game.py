#-----------------------------------------------------------------
#
# Guessing Game
#
# As an example of a program involving making a decision and
# user interaction, here you will develop a simple guessing
# game in a couple of stages.
#
# Stage 1
#
# Write code that :
#
# (a) chooses a random number between 0 and 9, inclusive;
# (b) prints a prompt asking the user to guess what the number is,
#     such as "What number am I thinking of?" or similar;
# (c) reads a number typed by the user; and
# (d) prints "You're right!" if the number typed by the user
#     is the same as the random number chosen, or "Sorry." if
#     the numbers do not match.
#
# To do this you will need the "randint" and "input" functions
# as well as an IF statement.
#
# Stage 2
#
# Having gotten the code outlined above to work, you can make
# the "game" more interesting by asking the user to guess
# several times and then keeping and displaying a total score.
# To do this you will need to
#
# (a) introduce a variable to keep track of the score and
#     increment it each time the user guesses correctly;
# (b) create a list of "guess numbers";
# (c) put a FOR loop around your code so that it is run
#     once for each guess number; and
# (d) display the score at the end.
#

# Import the random integer function
from random import randint

##### DEVELOP YOUR PROGRAM HERE

a_random_number = randint(0, 9)

amount_of_trys = range(10)

for guesses in amount_of_trys:
    promt = 'Guess the random number between 0 and 9!'
    command = input(promt)
    if a_random_number == command:
        print 'You''re right!'
    elif not a_random_number == command:
        print 'Sorry'
