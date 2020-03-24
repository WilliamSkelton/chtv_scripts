import glob
import os
import MySQLdb
import time
import requests 

host = "192.168.1.201"
user = "Kyle"
passwd = "OyqYrvV7RP6xLWpW"
db = "chtv_blockbuster"

apikey = "6c50c148"


def sql(query):
	#This Function facilitates simple SQL queries with no Variables. For Example SELECT queries
	conn = MySQLdb.connect(host, username, passwd, db)
	cursor = conn.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	conn.commit()
	conn.close()
	return result


def sqlVars(query, vars):
	#This Function facilitates more complex SQL calls that include Variables. For Example INSERT statements with WHERE clauses
	conn = MySQLdb.connect(host, username, passwd, db)
	cursor = conn.cursor()
	cursor.execute(query, [vars])
	result = cursor.fetchall()
	conn.commit()
	conn.close()
	return result


files = glob.glob("/mnt/import*.mkv")

for file in files:
	filepath = file
	filepath_components = file.split('/')
	filename = filepath_components[-1]
	title = filename.split("(")
	title = title[0]
	year = title[1].split(")")
	title.replace(" ", "+")

	searchtitleurl = f"http://www.omdbapi.com/?apikey={apikey}&t={title}&y={year}"
	response = requests.get(searchtitleurl)
	data = response.json()



	sqlVars("REPLACE INTO 'library' SET ")

