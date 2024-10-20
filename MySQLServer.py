import mysql.connector

try:

	db = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "root"
	)
	dbc = db.cursor()
	try:
		dbc.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
		print("Database 'alx_book_store' created successfully!")
	except mysql.connector.Error as e:
		print(f"Unable to Create Database: {e}")

except mysql.connector.Error as e:
	print(f"Failed to Connect to MySQL: {e}")

finally:
	if db.is_connected():
		dbc.close()
		db.close()



