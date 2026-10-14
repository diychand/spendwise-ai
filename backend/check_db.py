import sqlite3

conn = sqlite3.connect('spendwise.db')

count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()
income = conn.execute("SELECT SUM(amount) FROM transactions WHERE type='CREDIT'").fetchone()
expense = conn.execute("SELECT SUM(amount) FROM transactions WHERE type='DEBIT'").fetchone()
months = conn.execute("SELECT DISTINCT substr(date, 1, 7) FROM transactions ORDER BY 1").fetchall()

print("Total transactions:", count)
print("Total income:", income)
print("Total expense:", expense)
print("Distinct months:", months)
print("Month count:", len(months))

conn.close()