import mysql.connector as mc
import os

def Connector ():
	con = mc.connect(
		user="root", 
		password=os.environ("DB_PW"),
		host="mysql",
		database="test"
	)
	return con
