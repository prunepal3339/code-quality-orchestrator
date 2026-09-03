import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('scraped_data.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

# Function create table
def create_table(conn):
    try:
       c = conn.cursor()
       c.execute('''CREATE TABLE IF NOT EXISTS products
                    (id integer PRIMARY KEY,
                     name text NOT NULL,
                     price real);''')
    except Error:
       print(Error)

# Function to insert data into the table
def insert_product(conn, product):
    sql = ''' INSERT INTO products(name,price)
              VALUES(?,?) '''
    cur = conn.cursor() 
    cur.execute(sql, product)
    conn.commit()
    return cur.lastrowid

# Main function to scrape data and store in database
def main():
    url = 'https://example.com'  # Replace with your target URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming each product has a div with class 'product'
        products = soup.find_all('div', class_='product')
        
        conn = create_connection()
        
        if conn is not None:
            create_table(conn)
            
            for product in products:
                name = product.find('h2').text.strip()
                price = float(product.find('span', class_='price').text.strip().replace('$', ''))
                
                product_tuple = (name, price)
                insert_product(conn(product_tuple))
            
            conn.close()
        else:
            print("Error! cannot create the database connection.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == '__main__':
    main()
