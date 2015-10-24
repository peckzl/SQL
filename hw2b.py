#import sqlite3
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET quantity = 20 WHERE model = 'F150' ")
	c.execute("UPDATE inventory SET quantity = 100 WHERE model = 'Civic' ")

	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]