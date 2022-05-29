#cloud sql code#
import mysql.connector

# establishing the connection
conn = mysql.connector.connect(
    host = "34.101.110.162",       # e.g. '172.0.0.1'
    user = "root",            # e.g. 'user'
    password = "caca",        # e.g. 'password'
    database = "hewankudb"    # e.g. 'mydatabase'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Retrieving single row
sql = '''SELECT * from hewankusayang'''

# Executing the query
cursor.execute(sql)

# Fetching 1st row from the table
result = cursor.fetchone()
print(result)

# Closing the connection
conn.close()
