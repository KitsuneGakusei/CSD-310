import mysql.connector

# Try to connect to your MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # ← replace this
    database="movies"          # ← replace if you're using a different database
)

print("Connection successful!")

conn.close()
