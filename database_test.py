import table
def main():
    database = r"C:\Users\artur\Desktop\todolist_ca\todolist.db"
    conn = table.create_connection()
    if conn is not None:
        table.create_table(conn)
        table.add_row(conn, ('Do Elevate', 'personal'))
        table.add_row(conn, ('Walk with Kobe', 'Kobe'))
        table.add_row(conn, ('Apply for a job', 'personal'))
        table.add_row(conn, ('Call Mom', 'personal'))
        table.update_row(conn, ('COMPLETE',3))
    else:
        print('Error!')

if __name__ == '__main__':
    main()
    