import mysql.connector as sql
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

db = sql.connect(
  host="localhost",
  user="root",
  passwd="password",
  auth_plugin = 'mysql_native_password',
  database="testdatabase"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM Test WHERE gender = 'F' ")

for x in cursor:
  print(x)

