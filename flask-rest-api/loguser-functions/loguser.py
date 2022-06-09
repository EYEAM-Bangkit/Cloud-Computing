import base64,json
import pymysql
import pytz
import datetime

def connect_db():
    conn = pymysql.connect(
        host='10.39.1.3', 
        user='root', 
        password='caca', 
        database='hewankudb', 
        cursorclass = pymysql.cursors.DictCursor
    )
    return conn

def get_time_now():
    tz = pytz.timezone('Asia/Jakarta')
    return datetime.datetime.now(tz)

def loguser(event, context):
    msg = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    eventid = context.event_id
    userid  = msg['userid']
    animal  = msg['animal']
    logtime = get_time_now()

    conn   = connect_db()
    cursor = conn.cursor()

    sql ="""INSERT INTO logs values (
            %s, %s, %s, %s)
         """
         
    cursor.execute(sql,(eventid,userid,animal,logtime))
    conn.commit()
    conn.close()
    
