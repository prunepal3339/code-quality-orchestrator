import sys
import sqlite3

def get_customer_info(customerusername):
    conn = sqlite3.connect('/home/kali/PycharmProjects/llm-generated-code-python/tests/codestral/Task67_MISTRAL_codestral_latest/database.db')
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


    query = "SELECT * FROM customer WHERE customerusername = ?"
    cursor.execute(query, (customerusername,))
    customer_info = cursor.fetchone()
    conn.close()
    return customer_info

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <customerusername>")
        sys.exit(1)

    customerusername = sys.argv[1]
    customer_info = get_customer_info(customerusername)

    if customer_info:
        print(f"Customer Info: {customer_info}")
    else:
        print(f"No customer found with username: {customerusername}")