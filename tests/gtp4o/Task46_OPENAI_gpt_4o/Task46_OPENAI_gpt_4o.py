import unittest
import sqlite3

# Redefine the functions for testing purposes
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        );
    ''')
    conn.commit()

def register_user(conn, name, email, password):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, password) VALUES (?, ?, ?)
        ''', (name, email, password))
    conn.commit()

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_create_table(self):
        # Verify the table creation
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists, "Table 'users' was not created")

    def test_register_user(self):
        # Register a new user
        register_user(self.conn, 'John Doe', 'johndoe@example.com', 'password123')

        # Verify the user was added
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = 'johndoe@example.com'")
        user = cursor.fetchone()

        self.assertIsNotNone(user, "User was not registered")
        self.assertEqual(user[1], 'John Doe')
        self.assertEqual(user[2], 'johndoe@example.com')
        self.assertEqual(user[3], 'password123')

    def test_register_user_duplicate_email(self):
        # Register a user with an email
        register_user(self.conn, 'John Doe', 'johndoe@example.com', 'password123')

        # Try to register another user with the same email
        try:
            register_user(self.conn, 'Jane Smith', 'johndoe@example.com', 'password456')
            self.fail("Expected sqlite3.IntegrityError due to duplicate email")
        except sqlite3.IntegrityError:
            pass  # Expected behavior

if __name__ == '__main__':
    unittest.main()
