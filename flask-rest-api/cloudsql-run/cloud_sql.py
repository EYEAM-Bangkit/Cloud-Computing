import pymysql, base64
from config import *

def connect_db():
    connection = pymysql.connect(
        host     = sql_host, 
        user     = sql_user, 
        password = sql_password, 
        database = sql_database, 
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

def getSpeciesData(name):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM animal WHERE namapopuler LIKE '%{name}%' OR namailmiah LIKE '%{name}%'")

    result = cursor.fetchall()
    connection.close()
    return result

def getUserLogs(user_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM logs WHERE userid='{user_id}'")

    result = cursor.fetchall()
    connection.close()
    return result

# url safe solution to decode base64 to fix padding issues
def decode_base64(data):
    data += '=' * (len(data) % 4)
    return base64.urlsafe_b64decode(data)
