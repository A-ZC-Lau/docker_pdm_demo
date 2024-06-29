import sqlite3

con = sqlite3.connect("test.db")

con.execute("""
		CREATE TABLE tb(
			country VARCHAR(50),
			country_code VARCHAR(2),
			year INT,
			estimated_population_number INT,
			estimated_prevalence INT
		);
""")
