import cx_Oracle

try:
    connection=cx_Oracle.connect(
        user="scott",
        password="tiger",
        dsn="localhost:1521/XEPDB1",
        encoding="UTF-8"
    )
    print(connection.version)
    cursor=connection.cursor()
    cursor.execute("SELECT * from emp")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("End of connection")