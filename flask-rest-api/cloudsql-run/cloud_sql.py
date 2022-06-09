import pymysql

def connect_db():
    connection = pymysql.connect(
        host='10.39.1.3', 
        user='root', 
        password='caca', 
        database='hewankudb', 
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

def getSpeciesData(name):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler LIKE '%{name}%' OR namailmiah LIKE '%{name}%'")

    result = cursor.fetchall()
    connection.close()
    return result

def getUserLogs(user_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM user WHERE user_id=={user_id}")

    result = cursor.fetchall()
    connection.close()
    return result