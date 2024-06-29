from fastapi import FastAPI
import sqlite3
import requests
import csv
import json
import pandas
from io import StringIO

# con = sqlite3.connect("")

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

	print(len(j))
	print(j[0:3])
