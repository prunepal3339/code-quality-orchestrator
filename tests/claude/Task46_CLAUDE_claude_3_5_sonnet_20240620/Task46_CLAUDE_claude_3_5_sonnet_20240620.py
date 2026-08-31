import unittest
from unittest.mock import patch
from io import StringIO
import sqlite3

# Re-define the functions here for testing purposes
def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT, email TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()

def register_user(conn, name, email, password):
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        return "Registration successful!"
    except sqlite3.IntegrityError:
        return "Email already exists. Registration failed."

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Create a new in-memory database for each test
        self.conn = sqlite3.connect(':memory:')
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    @patch('builtins.input', side_effect=['John Doe', 'john@example.com', 'password123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_new_user(self, mock_stdout, mock_input):
        result = register_user(self.conn, 'John Doe', 'john@example.com', 'password123')
        output = mock_stdout.getvalue()
        self.assertIn("Registration successful!", result)

    @patch('builtins.input', side_effect=['Jane Doe', 'jane@example.com', 'password456'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_duplicate_email(self, mock_stdout, mock_input):
        register_user(self.conn, 'John Doe', 'john@example.com', 'password123')
        result = register_user(self.conn, 'Jane Doe', 'john@example.com', 'password456')
        output = mock_stdout.getvalue()
        self.assertIn("Email already exists. Registration failed.", result)

    def test_create_table(self):
        # Verify the table creation
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = c.fetchone()
        self.assertIsNotNone(table_exists, "Table 'users' was not created")

    def test_register_user_validity(self):
        # Test successful registration
        register_user(self.conn, 'Alice Smith', 'alice@example.com', 'password789')
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE email = 'alice@example.com'")
        user = c.fetchone()
        self.assertIsNotNone(user, "User was not registered")
        self.assertEqual(user[0], 'Alice Smith')
        self.assertEqual(user[1], 'alice@example.com')
        self.assertEqual(user[2], 'password789')

if __name__ == '__main__':
    unittest.main()
