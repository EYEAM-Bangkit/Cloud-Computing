#cloud sql code#
import json
from sqlalchemy import create_engine

# establishing the connection
engine = create_engine('mysql+mysqldb://root:caca@10.39.0.3:3306/hewankudb')
connection = engine.raw_connection()

# check the connection
if connection:
    print("Connected Successfully")
else:
    print("Connection Not Established")

# Fetching the data
def getSpeciesData(name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler = '{name}'")
    # Just change the column using "where"
    result = cursor.fetchone()
    return json.dumps(
        {
            "namapopuler": result[0],
            "namailmiah": result[1],
            "foto": result[2],          # Result index 2 must be a null foto
            "taxonomy": result[3],
            "kingdom": result[4],
            "genus": result[5],
            "class": result[6],
            "ordo": result[7],
            "family": result[8],
            "species": result[9],
            "deskripsi": result[10],
            "persebaran": result[11],
            "habitat": result[12],
            "iucn": result[13],
            "tersedia": result[14],
            "rataumur": result[15],
            "ratapanjang": result[16],
            "ratalebar": result[17],
            "rataberat": result[18]
        }
    )


print(getSpeciesData('nama2'))