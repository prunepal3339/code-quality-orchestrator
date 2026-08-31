import sqlite3
import sys

def get_customer_info(username):
    conn = sqlite3.connect('/home/kali/PycharmProjects/llm-generated-code-python/tests/gtp4o/Task67_OPENAI_gpt_4o/database.db')
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

    cursor.execute("SELECT * FROM customer WHERE customerusername = ?", (username,))
    customer = cursor.fetchone()
    conn.close()
    return customer

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <customerusername>")
        sys.exit(1)
    customer_username = sys.argv[1]
    customer_info = get_customer_info(customer_username)
    print(customer_info)