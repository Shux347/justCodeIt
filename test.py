import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',  # Replace with your MySQL root password
        database='mwh_db'          # Replace with your database name
    )
    print("Connected to MySQL successfully!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")