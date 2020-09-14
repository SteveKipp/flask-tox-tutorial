import sqlite3

class SQLiteDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('customers')
        self.c = self.conn.cursor()

    def get_all(self):
        self.c.execute('''SELECT * FROM customers;''')
        return self.c.fetchall()
