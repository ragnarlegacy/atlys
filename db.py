from google.cloud.sql.connector import Connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Cloud SQL Connector
connector = Connector()

def get_db_connection():
    """
    Establish a secure connection to the Cloud SQL MySQL instance using the Cloud SQL Connector.
    """
    connection = connector.connect(
        os.getenv("DB_CONNECTION_NAME","ragnar-07:us-central1:atlysdb"),  # e.g., "project:region:instance"
        "mysql",
        user=os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASSWORD","root123"),
        db=os.getenv("DB_NAME","user_db"),
    )
    connection.execute("""
            CREATE TABLE IF NOT EXISTS user (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                )      
    """)
    return connection

def close_connection(connection, cursor=None):
    """
    Close the database connection and cursor.
    """
    if cursor:
        cursor.close()
    if connection:
        connection.close()

def create_user(name, email):
    """
    Insert a new user into the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            ""
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        close_connection(conn, cursor)

def get_all_users():
    """
    Retrieve all users from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        close_connection(conn, cursor)
