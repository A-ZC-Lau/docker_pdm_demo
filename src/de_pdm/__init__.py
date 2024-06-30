from fastapi import FastAPI
import sqlite3
import mysql.connector as mc
import requests
from io import StringIO
import pandas

from ..db import db

app = FastAPI()

@app.get("/")
def read_root ():
	return {"Hello": "worldsdf"}

@app.get("/get")
def retrieve ():
	r = requests.get("https://public.tableau.com/app/sample-data/TB_Burden_Country.csv")
	dc = r.content.decode('utf-8')
	df = pandas.read_csv(StringIO(dc))
	j = df.to_dict("records")

	con = db.Connector("test")
	cur = con.cursor()

	for row in j[0:10]:
		query = """
			INSERT INTO tb(
				country,
				country_code,
				year,
				estimated_population_number,
				estimated_prevalence
			)
			VALUES (
				%s,
				%s,
				%s,
				%s,
				%s
			);
			"""
		country = row["Country or territory name"]
		countryCode = row["ISO 2-character country/territory code"]
		year = row["Year"]
		pop = row["Estimated total population number"]
		prev = row["Estimated prevalence of TB (all forms) per 100 000 population"]
		r = cur.execute(query, (country, countryCode, year, pop, prev))
		con.commit()
	
	con.close()
	# print(len(j))
	# print(j[0:3])
	return ("added %s") % (len(j))

@app.get("/view")
def view ():
	con = db.Connector("test")
	cursor = con.cursor()
	query = """SELECT * FROM tb LIMIT 10;"""
	cursor.execute(query)
	r = cursor.fetchall()
	con.close()
	return r
