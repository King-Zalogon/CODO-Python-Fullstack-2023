import sqlite3

DATABASE = 'myData.db'

def connect():
    connector = sqlite3.connect(DATABASE) # creates an object through the function that is our connector to the db.

    connector.row_factory = sqlite3.Row # A mix between an array and a dictionary
    # Allows to refer to the column by their number or their name

    return connector

#   CREATE TABLE    ------------

conn = connect()

cursor = conn.cursor() # Contains the data that comes and goes between py and db

my_sql_query = """
CREATE TABLE IF NOT EXISTS products (
        code INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        amount INTEGER NOT NULL,
        price REAL NOT NULL
    )
"""

cursor.execute(my_sql_query)

conn.commit() # Forces writing the info in the db, flushes the ram

cursor.close() # Always close after using
conn.close() # Always close after using


#   ADDING DATA    ------------

desc = "Mouse"
price = 3700
stock = 12

conn = connect()
cursor = conn.cursor()

my_sql_query = '''
INSERT INTO products
(description,amount,price)
VALUES(?,?,?)'''

cursor.execute(my_sql_query, (desc, stock, price))

conn.commit()
cursor.close()
conn.close()


#   MAKING A QUERY    ------------

conn = connect()
cursor = conn.cursor()
code = 2

my_sql_query = '''
SELECT * FROM products
WHERE code = ?
'''

cursor.execute(my_sql_query , (code,))
# Can create an array with one array or many arrays within

product = cursor.fetchone()
print(product["code"])
print(product["description"])
print(product["amount"])
print(product["price"])

conn.commit()
cursor.close()
conn.close()
