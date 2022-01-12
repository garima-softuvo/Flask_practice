import sqlite3

from flask import Flask, request, jsonify
import json
import os
app = Flask(__name__)

path = r"/home/softuvo/Garima/Flask Practice/Flask_practice/files"
files = os.listdir(path)
   
def convertToBinaryData():
    for f in files:
        print(f)
        filename=os.path.join(path, f)
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

convertToBinaryData()



















# file_path = os.listdir("/home/softuvo/Garima/Flask Practice/Flask_practice/files")
# def read_file(filename):
#     with open(filename, 'rb') as f:
#         photo = f.read()
#     return photo

# def insert_file(file_name, data, Employee):
#     try:
#         # Establish a connection
#         connection = sqlite_connect("data")
#         print(f"Connected to the database `{data}`")

#         # Create a cursor object
#         cursor = connection.cursor()

#         sqlite_insert_blob_query = f"""
#         INSERT INTO {Employee} (name, salary) VALUES (?, ?)
#         """

#         # Convert the file into binary
#         binary_file = convert_into_binary(file_name)
#         data_tuple = (file_name, binary_file)

#         # Execute the query
#         cursor.execute(sqlite_insert_blob_query, data_tuple)
#         connection.commit()
#         print('File inserted successfully')
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Failed to insert blob into the table", error)
#     finally:
#         if connection:
#             connection.close()
#             print("Connection closed")
# insert_file("sample.pdf", "data.sqlite", "Employee")




