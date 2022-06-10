import base64,json
import pymysql
import pytz
import datetime

from config import *

def connect_db():
    conn = pymysql.connect(
        host     = sql_host, 
        user     = sql_user, 
        password = sql_password, 
        database = sql_database, 
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

    print(f"eventid {eventid}, userid {userid}, animal {animal}, logtime {logtime}")

    conn   = connect_db()
    cursor = conn.cursor()

    sql ="""INSERT INTO logs values (
            %s, %s, %s, %s)
         """
         
    cursor.execute(sql,(eventid,userid,animal,logtime))
    conn.commit()
    conn.close()