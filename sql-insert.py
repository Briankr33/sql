import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()
	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers (value INT)")

	# create list of 100 random integers, ranging from 0-100
	for i in range(100):
		c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
