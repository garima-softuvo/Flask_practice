import sqlite3

conn = sqlite3.connect("dbtable.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE table(
    id integer PRIMARY KEY,
    name text NOT NULL,
    salary float NOT NULL
)"""
cursor.execute(sql_query)