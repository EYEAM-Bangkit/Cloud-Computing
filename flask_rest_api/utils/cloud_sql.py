#cloud sql code#
import json
import pymysql
import pymysql.cursors

# establishing the connection
connection = pymysql.connect(
    host='10.39.0.3',
    user='root',
    password='caca',
    database='hewankudb',
    cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()

# check the connection
if connection:
    print("Connected Successfully")
else:
    print("Connection Not Established")

# Fetching the data
def getSpeciesData(name):
        cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler = %s", name)
        # Just change the column using "where"
        result = cursor.fetchone() 
        # Result index 2 must be a null foto
        return result

print(getSpeciesData('nama2'))