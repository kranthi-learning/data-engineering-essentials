import psycopg2
from psycopg2 import OperationalError

# Define the connection parameters
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'DataEngineer2024',
    'host': 'localhost',  # Change to your host (e.g., 'localhost', '127.0.0.1', or a specific IP address)
    'port': '5432'        # Default PostgreSQL port, change if necessary
}

# Connect to the PostgreSQL server
try:
    connection = psycopg2.connect(**db_config)
    print("Connection successful!")

    # Create a cursor object using a context manager
    with connection.cursor() as cursor:
        # Example query to execute
        cursor.execute("SELECT version();")
        
        # Fetch the result
        db_version = cursor.fetchone()
        print(f"PostgreSQL version: {db_version[0]}")

except OperationalError as e:
    print(f"Error: {e}")
finally:
    # Close the connection if it was established
    if connection:
        connection.close()
        print("Connection closed.")