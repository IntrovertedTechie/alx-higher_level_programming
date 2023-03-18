#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # take arguments from command line
    mysql_username = "u0_a290"
    mysql_password = ""
    database_name = ""

    # connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # create cursor to execute queries
    cursor = db.cursor()

    # execute query to get all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # print the rows
    for row in rows:
        print(row)

    # close the cursor and database connection
    cursor.close()
    db.close()

