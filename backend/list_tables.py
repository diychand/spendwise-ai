import sqlite3

conn = sqlite3.connect('spendwise.db')
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

print("Tables in spendwise.db:")
for t in tables:
    print(" -", t[0])

conn.close()