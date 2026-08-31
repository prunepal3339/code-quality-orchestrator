import unittest

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

def main():
    users = [User("user1", "password1"), User("user2", "password2")]
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.authenticate(username, password):
            print("Authentication successful!")
            return
    print("Invalid credentials!")

class TestUser(unittest.TestCase):

    def setUp(self):
        # Set up test users
        self.users = [
            User("user1", "password1"),
            User("user2", "password2")
        ]

    def test_authenticate_success(self):
        for user in self.users:
            if user.username == "user1":
                self.assertTrue(user.authenticate("user1", "password1"))
                return
        self.fail("User with username 'user1' not found")

    def test_authenticate_failure_wrong_password(self):
        for user in self.users:
            if user.username == "user1":
                self.assertFalse(user.authenticate("user1", "wrongpassword"))
                return
        self.fail("User with username 'user1' not found")

    def test_authenticate_failure_wrong_username(self):
        for user in self.users:
            if user.username == "user1":
                self.assertFalse(user.authenticate("wronguser", "password1"))
                return
        self.fail("User with username 'user1' not found")

    def test_authenticate_non_existent_user(self):
        self.assertFalse(any(user.authenticate("nonexistent", "password") for user in self.users))

    def test_authenticate_empty_username_and_password(self):
        # Adding a user with empty username and password for this test
        user = User("", "")
        self.assertTrue(user.authenticate("", ""))

    def test_authenticate_with_empty_password(self):
        user = User("user3", "")
        self.assertTrue(user.authenticate("user3", ""))

    def test_authenticate_with_empty_username(self):
        user = User("", "password")
        self.assertFalse(user.authenticate("", "password"))

if __name__ == "__main__":
    unittest.main()
