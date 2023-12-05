import mysql.connector

db = mysql.connector.connect(
  host="34.133.80.212",
  user="root",
  password="]18j%T%J6'0U9y98",
  database="la_crime"
)

def execute_query(query):
    cursor = db.cursor(buffered=True)
    try:
        cursor.execute(query)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()

