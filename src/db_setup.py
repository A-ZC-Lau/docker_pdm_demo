import mysql.connector as mc


cn = mc.connect(
	user="root", 
	password="password", # do not do this in production
	host="mysql",
)
cur = cn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS `test`;")
cur.execute("USE `test`;")
cur.execute("DROP TABLE IF EXISTS tb;")
cur.execute("""
	CREATE TABLE tb(
		country VARCHAR(50),
		country_code VARCHAR(2),
		year INT,
		estimated_population_number INT,
		estimated_prevalence INT
	);
	""")
cn.commit()
cn.close()
