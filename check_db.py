from database import get_connection

conn = get_connection()
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM employee_predictions").fetchall()

print("TOTAL RECORDS:", len(rows))
for row in rows:
    print(tuple(row))

conn.close()
