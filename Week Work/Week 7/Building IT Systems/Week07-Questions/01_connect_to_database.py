#----------------------------------------------------------------------
#
# Check database connection
#
# This program retrieves and displays the database server version,
# in order to confirm that we can access the Airline database
# from a Python script.
#
# Before running this script you should read the instruction sheet,
# and use phpMyAdmin to create the Airline database from
# the script provided.  You need to put your database credentials
# in the call to the "connect" function below
#

# Import the Python-MySQL module.
from mysql.connector import *

# Alternative import statement for the older connector.
# from MySQLdb import *

# Create a connection using relevant values for the server name, username,
# password and database name.
connection = connect(host = "131.181.70.168",
                     user = "9499776",
                     database = "9499776",
                     password = "2wltmjQB")

# Get a cursor on the database.  This allows you to execute SQL
# queries and get the results.
airline_db = connection.cursor()

# Execute an SQL query which retrieves the version of the database
# management system.
airline_db.execute("SELECT VERSION()")

# Get the first row from the query's Result Set.
row = airline_db.fetchone()

# Display the first element of the row.
print "Server version: ", row[0]

# Close the cursor.
airline_db.close()

# Close the database connection.
connection.close()
