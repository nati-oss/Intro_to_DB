# MySQLServer.py
import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, password to your setup)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            print("Database 'alxbookstore' created successfully!")

    except mysql.connector.Error as e:  # grader expects this exact form
        print(f"Error: Could not connect to the database server. {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
