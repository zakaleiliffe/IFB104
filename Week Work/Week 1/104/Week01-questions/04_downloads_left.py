# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

track_cost = 120 # cost in cents for downloading 1 track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded



track_cost_in_dollars = 1.20

amount_spent_so_far = track_cost_in_dollars * num_downloaded

print 'amount spent so far:', amount_spent_so_far

balance_left = budget - amount_spent_so_far

print 'balance left:', balance_left

tracks_left = balance_left / track_cost_in_dollars 

print 'tracks left:', tracks_left

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

