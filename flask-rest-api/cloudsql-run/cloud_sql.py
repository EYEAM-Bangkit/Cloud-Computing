#cloud sql code#
import pymysql
import pymysql.cursors

# establishing the connection
def connect_db():
    connection = pymysql.connect(host='10.39.1.3', user='root', password='caca', database='hewankudb', cursorclass = pymysql.cursors.DictCursor)
    return connection

# Fetching the data
def getSpeciesData(name):
    connection = connect_db()
    cursor = connection.cursor()
    # Just change the column using "where"
    cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler LIKE '%{name}%' OR namailmiah LIKE '%{name}%'")
    result = cursor.fetchall()
    connection.close()
    return result

print(getSpeciesData('lemur'))