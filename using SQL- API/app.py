from sqlite3.dbapi2 import Cursor
from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("dbtable.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM table")
        dbtable= [
            dict(id=row[0], name=row[1], salary=row[2])
            for row in cursor.fetchall()
        ]
        if dbtable is not None:
            return jsonify(dbtable)



    if request.method == "POST":
        new_name = request.form["name"]
        new_salary = request.form["salary"]


    sql = """INSERT INTO book (author, language, title)
                VALUES (?, ?, ?)"""
    cursor = cursor.execute(sql, (new_author, new_lang, new_title))
    conn.commit()
    return f"Table with the id: 0 created successfully", 201

if __name__ == "__main__":
    app.run(debug=True)







