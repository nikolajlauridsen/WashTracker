import sqlite3 as lite
from datetime import datetime
import time

old_db = lite.connect("washbase.db")
old_c = old_db.cursor()

new_db = lite.connect("Wash.db")
new_c = new_db.cursor()

old_c.execute("SELECT * FROM wash where paid == 1")
old_paid_washes = old_c.fetchall()

old_c.execute("SELECT * FROM wash where paid == 0")
old_unpaid_washes = old_c.fetchall()

# Need a receipt to mark the washes I've already paid for
print("Inesrting transfer receipt")
current_day = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_c.execute("INSERT INTO Receipts VALUES (?, ?)", (None, current_day))

print("Inserting " + str(len(old_paid_washes)) + " paid washes")
for wash in old_paid_washes:
    # wash_date = datetime.utcfromtimestamp(wash[0]).strftime("%Y-%m-%d %H:%M:%S.%f")
    wash_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(wash[0]))
    print("Inserting paid wash made the: " + wash_date)
    new_c.execute("INSERT INTO Washes VALUES (?, ?, ?, ?)", (None, 1, wash_date, 10))

print("Inserting " + str(len(old_unpaid_washes)) + " unpaid washes")
for wash in old_unpaid_washes:
    # wash_date = datetime.utcfromtimestamp(wash[0]).strftime("%Y-%m-%d %H:%M:%S.%f")
    wash_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(wash[0]))
    print("Inserting unpaid wash made the: " + wash_date)
    new_c.execute("INSERT INTO Washes VALUES (?, ?, ?, ?)", (None, None, wash_date, 10))

new_db.commit()
