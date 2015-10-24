#import libraries
import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	#delete db table if exists
	c.execute("DROP TABLE if exists numbers")
	
	#create db table
	c.execute("CREATE TABLE numbers(num INT)")

	for i in range(100):
		c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
