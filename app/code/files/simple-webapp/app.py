import os
import MySQLdb
from flask import Flask
from MySQLdb import _mysql

app = Flask(__name__)

conn =MySQLdb.connect("192.168.122.31","appuser","appuser","employee_db")
cursor = conn.cursor()

@app.route("/")
def main():
    return "Hello guys"

@app.route('/r_f_db')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()
    return ",".join(result)


