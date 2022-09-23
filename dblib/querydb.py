from dbcon import cursor

def query(tablename, limit):
    cursor.execute("USE nycdata_db;")
    cursor.execute(f"SELECT * FROM {tablename} LIMIT {limit}")
    result = cursor.fetchall()
    for row in result:
        print(row)

query("offence", 5)