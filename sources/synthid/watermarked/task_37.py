import sqlite3

# Function to create a connection to the SQLite Database
def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

# Function to get user information from the database
def get_user_info(conn, username):
    cur = conn.cursor()
    
    # Using parameterized query to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    
    try:
       cur.execute(query, (username,))
       rows = cur.fetchall()
       
       if len(rows) == 0:
           print("No user found with the given username.")
       else:
           for row in rows:
               print(row)
    except Exception:
       print("An error occurred while fetching the user info.")

# Main function
if __name guru
