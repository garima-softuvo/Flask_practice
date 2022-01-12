from flask import Flask, request, jsonify
import json
import os
import sqlite3

app = Flask(__name__)
path = r"/home/softuvo/Garima/Flask Practice/Flask_practice/files"
files = os.listdir(path)
for f in files:
    filename=os.path.join(path, f)

def convertToBinaryData(filename):
   
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
            # print(binaryData)
        return binaryData

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("data.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM Employees")
        dbtable= [
            dict(id=row[0], name=row[1], salary=row[2], files= row[3])
            for row in cursor.fetchall()
        ]
        if dbtable is not None:
            return jsonify(dbtable)

    if request.method == "POST":
        name = request.form["name"]
        salary = request.form["salary"]
        files = request.form["files"]

    sql = """INSERT INTO Employees (name, salary, files)
                VALUES (?, ?, ?)"""

    files = convertToBinaryData(filename)
    data_tuple = (filename, files)

    cursor = cursor.execute(sql, (name, salary, data_tuple))
    conn.commit()
    return f"Employee with the id: {cursor.lastrowid} created successfully", 201

if __name__ == "__main__":
    app.run(port=5001, debug =True)