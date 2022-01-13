from rich.console import Console
from rich.table import Table
import table
import sqlite3

def print_table():
    database = r"C:\Users\artur\Desktop\todolist_ca\todolist.db"
    try:
        conn = sqlite3.connect('todolist.db')
        rows = table.extract_rows(conn)
        rich_table = Table(title='My To-Do List')
        rich_table.add_column('Task')
        rich_table.add_column('Type')
        rich_table.add_column('Status')
        for row in rows:
            rich_table.add_row(row[1], row[2], row[3])
        console = Console()
        console.print(rich_table)
    except:
        print('No database exists!')
    
if __name__ == '__main__':
    print_table()