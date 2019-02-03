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

    def save_changes(self):
        """Commit changes to the database"""
        self.conn.commit()

    def insert_wash(self):
        self.c.execute("INSERT INTO wash VALUES (?, ?)", (time.time(), 0))

    def get_history(self, paid=False):
        if paid:
            self.c.execute("SELECT * FROM wash")
        else:
            self.c.execute("SELECT * FROM wash WHERE paid == 0")
        history = self.c.fetchall()
        return history

    def remove_entry(self, timestamp):
        self.c.execute("DELETE FROM wash WHERE added == (?)", (timestamp, ))

    def mark_all_as_paid(self):
        self.c.execute("UPDATE wash SET paid=1")

    def mark_as_paid(self, quantity):
        self.c.execute("UPDATE wash SET paid = 1 WHERE added IN (SELECT added FROM wash WHERE paid = 0 ORDER BY added ASC LIMIT (?))",
                       (quantity, ))
