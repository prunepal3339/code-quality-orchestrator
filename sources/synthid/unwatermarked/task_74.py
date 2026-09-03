import psycopg2

def get_db_connection():
    try:
        # Replace these values with your actual PostgreSQL database credentials
        dbname = "your_database_name"
        user = "your_username"
        password = "your_password"
        host = "your_host"  # This could be 'localhost' if your database is on the same machine
        port = "5432"  # Default PostgreSQL port

        # Establishing the connection
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        print("Connection established successfully")
        return conn

    except 경우 as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        # Perform database operations here
        # For example, creating a cursor and executing a query
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"My PostgreSQL database version: {db_version}")

        # Don't forget to close the cursor and connection when done
        cursor.close()
        connection.close()
