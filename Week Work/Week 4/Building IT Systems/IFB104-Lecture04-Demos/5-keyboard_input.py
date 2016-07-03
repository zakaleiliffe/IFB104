# Keyboard input
#
# This short demo highlights the difference between Python's raw_input
# and input functions.  Just run this file and respond to the prompts.

text = raw_input('Enter some alphabetic text: ')
print 'You entered "' + text + '" which is of type', type(text)
print
number = raw_input('Enter a number: ')
print 'You entered "' + number + '" which is of type', type(number)
print
text = input('Enter some alphabetic text IN QUOTES: ')
print 'You entered "' + text + '" which is of type', type(text)
print
number = input('Enter a number (no quotes): ')
print 'You entered', number, 'which is of type', type(number)

# Notice that when we were confident that we had a string value
# (assuming the user is well-behaved) we used the string
# concatentation operator "+".
