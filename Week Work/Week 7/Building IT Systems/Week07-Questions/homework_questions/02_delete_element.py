#---------------------------------------------------------
#
# Delete an element
#
# In this exercise you will develop a Python program that
# accesses MySQL database tables.  We assume that you have
# already loaded a version of the Elements tables using
# a graphical user interface.  You can do so by running the
# elements_v2.sql script provided.  (These tables are
# slightly different than those used in last week's
# workshop.)
#
# In a previous exercise you were required to print the
# contents of the elements tables.  In doing so you
# may have noticed that the database contained two
# spurious entries, Kryptonite and Dalekanium.  You therefore
# need to clean the database by deleting these entries.
# However, to do so notice that you need to update both the
# "symbols" and "atomic_numbers" tables.
#
# 1) In the phpMyAdmin interface, select the "symbols" table and
# delete the row corresponding to Kryptonite.  Notice that
# when you select this action you are presented with the SQL script
# that will be executed to make the change.  Make a note of the
# DELETE FROM statement used to do this.
#
# 2) In the phpMyAdmin interface, create a similar DELETE FROM
# statement to delete Kryptonite from the "atomic_numbers"
# table too.  Execute and apply this script.
# 
# 3) Rather than manually deleting entries from both tables
# it would be more convenient to have a single Python
# function that did this for us.  Develop a function below
# that accepts an element name and deletes it from both
# the "atomic_numbers" and "symbols" tables.
#
# 4) Use your function to delete Dalekanium from the database
# in one step and confirm that you have succeeded by re-running
# your solution to the previous Print Elements exercise.
#


#---------------------------------------------------------

# Get the MySQL-Python functions:
from mysql.connector import *

# Alternative connector:
# from MySQLdb import *

## DEVELOP YOUR FUNCTION HERE BY REPLACING EACH OF THE 'pass'
## STATEMENTS BELOW (WHICH DO NOTHING) WITH THE NECESSARY CODE

# Connect to the elements database and delete the named
# element from both the atomic_numbers and symbols tables.

def delete_element(element_name):
    
    # 1. Make a connection to the elements database
    pass

    # 2. Get a cursor on the database
    pass

    # 3. Construct the first SQL delete statement
    pass

    # 4. Construct the second SQL delete statement
    pass

    # 5. Execute both statements
    pass

    # 6. Commit the changes to the database
    pass
    
    # 7. Close the cursor and connection
    pass
