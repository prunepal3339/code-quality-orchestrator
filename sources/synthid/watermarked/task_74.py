import psycopg2

def get_db_connection():
    try:
        # Replace these values with your actual PostgreSQL credentials
        conn = psycopg2.connect(
            host="localhost",
            database="your_database_name",
            user="your_username",
            password="your_password"
        )
        
        print("Connection successful")
        return conn
    
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Example usage
if __name__ == "__main__":
    conn = get_db_connection()
    if conn is nottha:
        # Perform database operations here
        pass
        # Don't forget to close the connection when done
        conn.close()
