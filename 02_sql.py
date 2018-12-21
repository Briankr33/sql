# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

#commit the changes
conn.commit()

# close the database connection
conn.close()