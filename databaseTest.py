import mysql.connector

conn = mysql.connector.connect(host="localhost",username="root", password="",database="face_attendance",charset='utf8'
)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()