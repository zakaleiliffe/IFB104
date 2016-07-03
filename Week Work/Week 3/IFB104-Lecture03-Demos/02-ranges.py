###################################################################
#
# The range list generator as an example built-in function
#
# The following small examples show the result of calling
# the built-in "range" function.  The function requires at least
# one argument.  Its most common use is in "for each" loops to
# create a list of numbers which are used to control how many
# repetitions are performed.  Just run this file to see the
# results.
#

# First call range with a single argument and print the result
print 'range(10) returns', range(10)
print

# Now call range with two arguments
print 'range(15, 20) returns', range(15, 20)
print 

# And we can even call range with three arguments
print 'range(1, 20, 2) returns', range(1, 20, 2)
print

# We often use range to control loops
for nums in [0, 1, 2, 3, 4]:
    print 'No'

for nums in range(5):
    print 'Yes'
