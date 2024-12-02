import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self):
        try:
            # Initialize MySQL database connection
            self.connection = mysql.connector.connect(
                host="localhost",       # Replace with your MySQL server host
                user="root",            # Replace with your MySQL username
                password="password",    # Replace with your MySQL password
                database="user_db"      # Replace with your database name
            )
            self.cursor = self.connection.cursor(dictionary=True)
            # Ensure the `user` table exists
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS user (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                )
            """)
            self.connection.commit()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def get_cursor(self):
        """Return the database cursor."""
        return self.cursor

    def get_connection(self):
        """Return the database connection."""
        return self.connection
