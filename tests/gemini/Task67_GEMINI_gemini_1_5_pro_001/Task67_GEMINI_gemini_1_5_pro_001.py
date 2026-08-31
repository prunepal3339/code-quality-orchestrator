import sqlite3
import sys

def get_customer_info(customerusername):
    conn = sqlite3.connect('/home/kali/PycharmProjects/llm-generated-code-python/tests/gemini/Task67_GEMINI_gemini_1_5_pro_001/your_database.db')  # Replace 'your_database.db'
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS customer")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customerusername TEXT NOT NULL,
                    name TEXT,
                    email TEXT,
                    phone TEXT
                )
            ''')
    cursor.execute('''
                INSERT INTO customer (customerusername, name, email, phone)
                VALUES (?, ?, ?, ?)
            ''', ('mohammad', 'Mohammad Kadoumi', 'mohammad@example.com', '0598914376'))

    cursor.execute("SELECT * FROM customer WHERE customerusername=?", (customerusername,))
    customer_data = cursor.fetchone()

    conn.close()

    if customer_data:
        customer_info = {
            'customerusername': customer_data[0],
            'customerfirstname': customer_data[1],
            # Add other fields as needed
        }
        return customer_info
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <customerusername>")
        sys.exit(1)

    customerusername = sys.argv[1]
    print(customerusername)
    customer_info = get_customer_info(customerusername)

    if customer_info:
        print(customer_info)
    else:
        print(f"No customer found with username: {customerusername}")