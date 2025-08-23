# MySQLServer.py
import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE alxbookstore")
        print("Database alxbookstore created successfully")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
