import glob
import os
import MySQLdb
import time

host = "192.168.1.201"
user = "Kyle"
passwd = "FA46LCWHbhoPSHUy"
db = "chtv_blockbuster"

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