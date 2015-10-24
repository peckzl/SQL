#Insert command with error handler


#import the sqlite3 libary
import sqlite3

#creat the connection object
conn = sqlite3.connect("new.db")

#get a cursor object
cursor = conn.cursor()

try:
	#insert data
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

	#commit the changes
	conn.commit()
except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again..."

#close the db connection
conn.close()