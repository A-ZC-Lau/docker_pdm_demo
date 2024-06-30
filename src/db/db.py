import mysql.connector as mc
import os

def Connector (database=None):
	con = mc.connect(
		user="root", 
		password=os.environ["DB_PW"],
		host="mysql",
		database=database
	)
	return con
