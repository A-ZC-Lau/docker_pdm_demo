import sqlite3

con = sqlite3.connect("test.db")
cursor = con.cursor()

con.set_trace_callback(print)

cursor.execute("DROP TABLE IF EXISTS tb;")
con.commit()
cursor.execute("""
		CREATE TABLE tb(
			country VARCHAR(50),
			country_code VARCHAR(2),
			year INT,
			estimated_population_number INT,
			estimated_prevalence INT
		);
""")
con.commit()
con.close()
