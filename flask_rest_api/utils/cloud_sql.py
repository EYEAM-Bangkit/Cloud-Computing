#cloud sql code#
import mysql.connector
import json

# establishing the connection
conn = mysql.connector.connect(
    host = "10.39.0.3",       # e.g. '172.0.0.1'
    user = "root",            # e.g. 'user'
    password = "caca",        # e.g. 'password'
    database = "hewankudb"    # e.g. 'mydatabase'
)

# check the connection
if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")

# Fetching the data
def getSpeciesData(name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler = '{name}'")
    # Just change the column using "where"
    result = cursor.fetchone() 
    # Result index 2 must be a null foto
    return json.dumps({"namapopuler": result[0], "namailmiah": result[1], "foto": result[2], "taxonomy": result[3], "kingdom": result[4], "genus": result[5], "class": result[6], "ordo": result[7], "family": result[8], "species": result[9], "deskripsi": result[10], "persebaran": result[11], "habitat": result[12], "iucn": result[13], "tersedia": result[14], "rataumur": result[15], "ratapanjang": result[16], "ratalebar": result[17], "rataberat": result[18]})

print(getSpeciesData('nama2'))