# sql.py

import pyodbc

class SQL:
    def __init__(self):
        self.server = 'DESKTOP-9HC32H2\SQLEXPRESS'
        self.database = 'matchmaking'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.connection = pyodbc.connect(
            f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()

    def execute(self, query,params=None):
        if params:
            self.cursor.execute(query, params)
        else:    
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
