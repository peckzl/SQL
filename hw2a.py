#import sqlite3 libary
import sqlite3

#create connection
conn = sqlite3.connect("cars.db")

#get cursor
cursor = conn.cursor()

#insert data 
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'F150', 11)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 12)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 13)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 14)")

#commit the changes 
conn.commit()

#close the database connection
conn.close()