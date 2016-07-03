#----------------------------------------------------------------
#
# Access Denied
#
# As an example of making a fragile IT system robust, in this
# exercise you will prevent a program that accesses a database
# from crashing under different circumstances.
#
# NB: Before you can complete this exericse you need to create
# the "car_details" table by importing and running the
# "car_details.sql" script in the phpMyAdmin interface.
#
# The program below provides a simple textual interface to
# used car table.  It prompts the user to enter an SQL
# query, runs the query, and then prints the results.
#
# Some queries the user may want to enter are as follows:
#
#     SELECT DISTINCT make FROM car_details
#
#     SELECT DISTINCT model FROM car_details WHERE make = 'HOLDEN'
#
#     SELECT make, model FROM car_details WHERE seriesYear = '1968'
#
#     SELECT carId, make FROM car_details WHERE engineSize = '1.5L'
#
# However, this program can be caused to crash in (at least) a
# couple of ways.  Firstly, the attempt to connect to the
# database will fail if the hostname or any of the user
# credentials are incorrect.  Secondly, the attempt to execute
# the SQL query will fail if the user enters invalid SQL code.
#
# Your task is to use exception handling to stop the program
# crashing in either of these circumstances.  Firstly run the
# program to find out which exceptions are thrown by these
# problems.  Then add "TRY ... EXCEPT ..." code in appropriate
# locations to allow the program to either continue executing
# or terminate gracefully if one of these errors occurs.
#
# Note that if you cannot connect to the database then there
# is little your program can do other than alert the user and
# terminate.  However, if the user enters an incorrect SQL
# query the program can recover and continue running.
#


#----------------------------------------------------------------

# Import the MySQL-Python connector functions
from mysql.connector import *

# Alternative MySQL-Python connector
# from MySQLdb import *

# Connect to the database
connection = connect(host='131.181.70.168',
                     user='9876543',
                     database='9876543',
                     password='???')

# Get a cursor into the database
cars_db = connection.cursor()

# Get queries from the user and execute them
query = raw_input('Enter an SQL query on the Used Cars data: ')

while not query.lower() in ['stop', 'exit', 'quit']:
    # Execute the query
    cars_db.execute(query)
    # Display the results
    for row in cars_db.fetchall():
        for cell in row:
            print cell,
        print
    # Get the next query
    print
    query = raw_input('Enter an SQL query on the Used Cars data: ')
    
# Unlock the database
cars_db.close()
connection.close()
