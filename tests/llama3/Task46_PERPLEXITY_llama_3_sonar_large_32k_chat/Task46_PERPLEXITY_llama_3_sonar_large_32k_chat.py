import unittest
import sqlite3

# Redefine functions for testing purposes
def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT, email TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()

def register_user(conn, name, email, password):
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, password))
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
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = c.fetchone()
        self.assertIsNotNone(table_exists, "Table 'users' was not created")

    def test_register_user_success(self):
        # Register a new user
        register_user(self.conn, 'John Doe', 'johndoe@example.com', 'password123')

        # Verify the user was added
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE email = 'johndoe@example.com'")
        user = c.fetchone()

        self.assertIsNotNone(user, "User was not registered")
        self.assertEqual(user[0], 'John Doe')
        self.assertEqual(user[1], 'johndoe@example.com')
        self.assertEqual(user[2], 'password123')

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
