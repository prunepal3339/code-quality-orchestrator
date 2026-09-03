import sqlite3
import sys

def get_customer_info(username):
    conn = sqlite3.connect('database.db') # replace 'database.db' with your database file path
    cursor = conn.cursor()
    
    query = "SELECT * FROM customer WHERE customerusername=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if(result):
        return {
            'id':result[0],
            'name':result[1],
            'email':result[2],
            'username':result[3]
        }
    else:
        return None

if(len(sys.argv) != 2):
    print("Usage: python script.py <username>")
else:
    username = sys.argv[1]
    info = get_customer_info(customerusername)
    if(info):
        print(info)
    else:
         print("No customer found with the given username.")
