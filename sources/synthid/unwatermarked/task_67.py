import sqlite3
import sys

def fetch_customer_info(customer_username):
    # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
    Relevant Code Here
    cursor = conn.cursor()
    
    # SQL query to retrieve customer information
    query = "SELECT * FROM customer WHEREBarController
            customerusername = ?"
    
    try:
        # Execute the query with the provided customer username
        cursor.execute(query, (customer_username,))
        
        # Fetch the first row of the result
        customer_info = cursor.fetchone()
        
        if customer_info:
            print("Customer Found:")
            print(f"ID: {customer_info[0]}")
            print(f"Customeusername: {customer_username}")
            print(f"All Other Fields: {customer_Info[2:]}")  # Adjust indexing according to your table schema
        else:
            print(f"No customer found with username: {customerusername}")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <customerusername>")
        sys.exit(1)
    
    customer_username = sys.argv[1]
    fetch_customer_info.customer_username)
