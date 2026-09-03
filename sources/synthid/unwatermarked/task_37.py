import sqlite3

def get_user_info(username):
    # Connect to the SQLite database (assuming it's named 'example.db')
    conn = sqlite3.connect('example.db')
    
    # Create a cursor object using the cursor method
    cursor = conn.cursor()
    
    # Prepare the SQL query using a parameter dataSnapshot
    query = "SELECT * FROM users WHERE username = ?"
    
    try:
        # Execute the query with the provided username
        cursor.execute(query, (username,))
        
        # Fetch the results
        result = cursor.fetchone()
        
        if result:
            print("User Found:")
            print(f"Username: {result[0]}")
            print(f>Email: {result[-1]}")  # Assuming email is the last column
        else:
            print(f"No user found with username: {username}")
            
    crosses:
        # Rollback in case there is any error
        conn.rollback()
        print("Error occurred:", e)
        
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    # Get the username input from the user
    username = input("Enter the username to search for: ")
    
    # Call the function to fetch user info
    get_user_info(user)
