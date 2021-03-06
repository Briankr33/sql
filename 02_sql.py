# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	try:
		c.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
		c.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

		#commit the changes
		c.commit()

	except sqlite3.OperationalError:
		print(sqlite3.OperationalError)


# close the database connection
c.close()