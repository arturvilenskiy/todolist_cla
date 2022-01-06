import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_row(conn, add_row_sql, task):
    cur = conn.cursor()
    cur.execute(add_row_sql, task)
    conn.commit()
    
    return cur.lastrowid

def update_row(conn, update_row_sql, task):
    cur = conn.cursor()
    cur.execute(update_row_sql, task)
    conn.commit()