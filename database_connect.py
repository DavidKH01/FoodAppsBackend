import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
connect = cursor = db = None

def connect():
    global connect, cursor, db
    try:
        connect = psycopg2.connect(
            host="localhost",
            database="postgres",
            user=os.environ.get('DB_USER'),
            port="5432",
            password=os.environ.get('DB_PASSWORD'))
        cursor = connect.cursor()
        db = cursor.execute()
    except (Exception, psycopg2.DatabaseError) as error:
        if connect:
            connect.rollback()
        print(error)


def get_db():
    if not (connect and cursor and db):
        connect()
    return connect, cursor, db


# cur.execute('SELECT * FROM restaurants')
# print(cur.fetchall())
#
# conn.commit()
#
# cur.close()
# conn.close()
