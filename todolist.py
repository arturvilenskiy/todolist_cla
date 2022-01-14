from rich.console import Console
from rich.table import Table
import table
import sqlite3
import os
import sys

database = r"C:\Users\artur\Desktop\todolist_ca\todolist.db"

def print_table():
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

def help():
    print('to check your todolist, type python todolist.py')
    print('to add a new task, type python todolist.py -a following by the task name and the type of the task')
    print('to complete an existing task, type python todolist.py -c following by the index of the task, starting at 1')

def add_task(taskName, taskType):
    conn = sqlite3.connect('todolist.db')
    table.add_row(conn, (taskName, taskType))

def complete_task(index):
    conn = sqlite3.connect('todolist.db')
    table.update_row(conn, ('COMPLETE',index))

def main():
    if len(sys.argv) == 1:
        print_table()
    elif sys.argv[1] == '-h':
        help()
    elif sys.argv[1] == '-a':
        string = ''
        for i in range(2, len(sys.argv)-1):
            string = string + sys.argv[i] + ' '
        add_task(string, sys.argv[-1])
    elif sys.argv[1] == '-c':
        complete_task(sys.argv[2])

if __name__ == '__main__':
    main()