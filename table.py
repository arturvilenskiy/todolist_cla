import sqlite3
from sqlite3 import Error

create_table_sql = """CREATE TABLE IF NOT EXISTS todolist (
                            id integer PRIMARY KEY,
                            task text NOT NULL,
                            type text NOT NULL,
                            status text NOT NULL);"""

add_row_sql = """INSERT INTO todolist (task, type, status)
                 VALUES(?,?,'NOT COMPLETE')"""

update_row_sql = """UPDATE todolist 
                    SET status = ?
                    WHERE id = ?"""

extract_rows_sql = """SELECT * FROM todolist"""
                    
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('todolist.db')
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def add_row(conn, task):
    try:
        cur = conn.cursor()
        cur.execute(add_row_sql, task)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

def update_row(conn, task):
    try:
        cur = conn.cursor()
        cur.execute(update_row_sql, task)
        conn.commit()
    except Error as e:
        print(e)
    
def extract_rows(conn):
    try:
        cur = conn.cursor()
        cur.execute(extract_rows_sql)
        records = cur.fetchall()
        return records
    except Error as e:
        print(e)