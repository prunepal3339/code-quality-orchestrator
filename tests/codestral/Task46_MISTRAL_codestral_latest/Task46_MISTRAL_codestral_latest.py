import unittest
import sqlite3

# Re-define the function and database setup for testing
def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT, email TEXT, password TEXT)''')
    conn.commit()

def register_user(conn, name, email, password):
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, password))
    conn.commit()

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database and set up the table
        self.conn = sqlite3.connect(':memory:')
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_register_user(self):
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

    def test_register_user_multiple_entries(self):
        # Register multiple users
        register_user(self.conn, 'John Doe', 'johndoe@example.com', 'password123')
        register_user(self.conn, 'Jane Smith', 'janesmith@example.com', 'password456')

        # Verify both users were added
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE email IN ('johndoe@example.com', 'janesmith@example.com')")
        users = c.fetchall()

        self.assertEqual(len(users), 2, "Not all users were registered")
        self.assertIn(('John Doe', 'johndoe@example.com', 'password123'), users)
        self.assertIn(('Jane Smith', 'janesmith@example.com', 'password456'), users)

if __name__ == '__main__':
    unittest.main()
