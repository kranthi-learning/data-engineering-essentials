import mysql.connector

# Define MySQL connection parameters
config = {
    'host': 'localhost',           # MySQL server host (use 'localhost' if running on the same machine)
    'user': 'newmysqluser',                # MySQL username
    'password': 'password123',   # MySQL password
    'database': 'newmysqluserdb'    # Name of the database you want to connect to
}

# Establish the connection
try:
    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        print("Successfully connected to MySQL database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Example query: Show all tables in the database
        cursor.execute("SHOW TABLES;")
        
        # Fetch and display the result
        tables = cursor.fetchall()
        print("Tables in database:")
        for table in tables:
            print(table)
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    # Close the cursor and connection to MySQL database
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")