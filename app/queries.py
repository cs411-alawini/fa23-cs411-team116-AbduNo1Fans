import mysql.connector

db = mysql.connector.connect(
  host="34.133.80.212",
  user="root",
  password="?7ng72rXO%S&K_|3",
  database="la_crime"
)

def execute_query(*args):
    cursor = db.cursor(buffered=True)
    try:
        cursor.execute(*args)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        
if __name__ == "__main__":
    print(execute_query("SELECT * FROM Users"))