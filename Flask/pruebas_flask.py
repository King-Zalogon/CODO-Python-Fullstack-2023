import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

# Name of flask object.
app = Flask(__name__)
CORS(app)


# Name of the file containing the database.
DATABASE = "testing_database.db"

#----------------------------------------------
# Connects to database. 
# Returns the connector (conn)
#----------------------------------------------
def connector():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


#----------------------------------------------
# Creates the "products" table in the
# data base, if it does exists already.
#----------------------------------------------
def create_table():
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    code INT PRIMARY KEY,
                    description VARCHAR(255),
                    stock INT,
                    price FLOAT)
            """)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()
    app.run()