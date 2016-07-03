# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python command "print E" will print the value of expression E


carton_of_milk = 1.25 * 2
mars_bar = 1.20 * 5
pkt_indigestion_tablets = 3.50 *1

money_given = 20.00

total = carton_of_milk + mars_bar + pkt_indigestion_tablets

print 'Cost of all items:', total

change_given = money_given - total

print 'Amount of change given:', change_given

