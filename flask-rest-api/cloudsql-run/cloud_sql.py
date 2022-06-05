#cloud sql code#
import pymysql
import pymysql.cursors

# establishing the connection
def connect_db():
    connection = pymysql.connect(host='34.101.110.162', user='root', password='caca', database='hewankudb', cursorclass = pymysql.cursors.DictCursor)
    return connection

# Fetching the data
def getSpeciesData(name):
    connection = connect_db()
    cursor = connection.cursor()
    # Just change the column using "where"
    cursor.execute('SELECT * FROM hewankusayang WHERE namailmiah = %s', name)
    result = cursor.fetchone()
    connection.close()
    return result

print(getSpeciesData('alami'))