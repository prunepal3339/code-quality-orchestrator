import unittest
import sqlite3
from unittest.mock import patch
from io import StringIO

# Redefine the function for testing
def register_user(conn, name, email, password):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        return "Registration successful!"
    except sqlite3.IntegrityError:
        return "Error: Email already exists."
    finally:
        conn.close()

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')

    def tearDown(self):
        self.conn.close()

    @patch('builtins.input', side_effect=['Alice', 'alice@example.com', 'password123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_user_success(self, mock_stdout, mock_input):
        result = register_user(self.conn, 'Alice', 'alice@example.com', 'password123')
        output = mock_stdout.getvalue()
        self.assertEqual(result, "Registration successful!")
        self.assertIn("Registration successful!", output)

        # Verify the user is actually registered
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = 'alice@example.com'")
        user = cursor.fetchone()
        self.assertIsNotNone(user, "User was not registered")
        self.assertEqual(user[1], 'Alice')
        self.assertEqual(user[2], 'alice@example.com')
        self.assertEqual(user[3], 'password123')

    @patch('builtins.input', side_effect=['Bob', 'alice@example.com', 'password456'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_user_duplicate_email(self, mock_stdout, mock_input):
        # First, register a user
        register_user(self.conn, 'Alice', 'alice@example.com', 'password123')

        # Try to register another user with the same email
        result = register_user(self.conn, 'Bob', 'alice@example.com', 'password456')
        output = mock_stdout.getvalue()
        self.assertEqual(result, "Error: Email already exists.")
        self.assertIn("Error: Email already exists.", output)

if __name__ == '__main__':
    unittest.main()
