import sqlite3
from bs4 import BeautifulSoup
import requests

# Set up the SQLite database and cursor
connection = sqlite3.connect('scraped_data.db')
cursor = connection.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS data_table 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              content TEXT)''')

# Specify the URL to scrape
url = 'https://example.com'

# Send a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the desired data from the webpage
# For this example, let's assume we want to extract all <p> tags
data = soup.find_all('p')

# Insert the extracted data into the SQLite database
for item in data:
    cursor.execute("INSERT INTO data_table (title, content) VALUES (?,?)", ('', str(item.text)))

# Commit changes and close the database connection
connection.commit()
connection.close()
