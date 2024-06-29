from fastapi import FastAPI
import sqlite3
import requests
import csv
import json
import pandas
from io import StringIO

r = requests.get("https://public.tableau.com/app/sample-data/TB_Burden_Country.csv")
dc = r.content.decode('utf-8')
df = pandas.read_csv(StringIO(dc))
j = df.to_dict("records")

print(len(j))
print(j[0:3])
