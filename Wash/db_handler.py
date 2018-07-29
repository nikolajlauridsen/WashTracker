"""
Class which handles database interaction
"""
import sqlite3 as lite
import time
from Wash import DB_NAME


class DbHandler:
    """Handles Database interaction"""

    def __init__(self):
        self.conn = lite.connect(DB_NAME)
        self.c = self.conn.cursor()
        for qry in open('schema.sql', 'r').readlines():
            self.c.execute(qry)
        print('Database set up...')

    def save_changes(self):
        """Commit changes to the database"""
        self.conn.commit()

    def insert_wash(self):
        self.c.execute("INSERT INTO wash VALUES (?, ?)", (time.time(), 0))

    def get_history(self):
        self.c.execute("SELECT * FROM wash WHERE paid == 0")
        history = self.c.fetchall()
        return history

    def remove_entry(self, timestamp):
        self.c.execute("DELETE FROM wash WHERE added == (?)", (timestamp, ))

    def mark_all_as_paid(self):
        self.c.execute("UPDATE wash SET paid=1")
