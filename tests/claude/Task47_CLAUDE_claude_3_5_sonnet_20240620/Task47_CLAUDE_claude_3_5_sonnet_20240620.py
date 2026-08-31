import unittest
import sqlite3
from unittest.mock import patch, MagicMock
from io import StringIO

# Redefine functions for testing purposes
def scrape_website(url):
    # Function to scrape data from website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Example: scraping all paragraph texts
    data = [p.text for p in soup.find_all('p')]
    return data

def store_in_database(conn, data):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scraped_text
                 (id INTEGER PRIMARY KEY, content TEXT)''')
    for item in data:
        c.execute("INSERT INTO scraped_text (content) VALUES (?)", (item,))
    conn.commit()

class TestWebScrapingAndDatabase(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.scraped_data = ['Paragraph 1', 'Paragraph 2', 'Paragraph 3']

    def tearDown(self):
        self.conn.close()

    @patch('requests.get')
    def test_scrape_website(self, mock_get):
        # Mock the response object for requests.get
        mock_response = MagicMock()
        mock_response.content = '''
        <html>
            <body>
                <p>Paragraph 1</p>
                <p>Paragraph 2</p>
                <p>Paragraph 3</p>
            </body>
        </html>
        '''
        mock_get.return_value = mock_response

        url = "https://example.com"
        data = scrape_website(url)

        self.assertEqual(data, ['Paragraph 1', 'Paragraph 2', 'Paragraph 3'])

    def test_store_in_database(self):
        store_in_database(self.conn, self.scraped_data)

        # Verify the data was stored
        c = self.conn.cursor()
        c.execute("SELECT content FROM scraped_text")
        stored_data = [row[0] for row in c.fetchall()]

        self.assertEqual(stored_data, self.scraped_data)

if __name__ == '__main__':
    unittest.main()
