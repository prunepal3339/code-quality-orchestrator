
import getpass
import unittest


def authenticate(username,password):
    # username = input("Enter username: ")
    # password = getpass.getpass("Enter password: ")
    return username == "admin" and password == "password123"

def access_resource(resource):
    if resource == "1":
        print("Accessing confidential files...")
    elif resource == "2":
        print("Accessing financial records...")
    elif resource == "3":
        print("Accessing employee database...")
    else:
        print("Invalid resource selection.")

def main():
    if authenticate():
        print("Authentication successful.")
        while True:
            print("\\nAvailable resources:")
            print("1. Confidential files")
            print("2. Financial records")
            print("3. Employee database")
            print("4. Exit")
            choice = input("Enter resource number to access (or 4 to exit): ")
            if choice == "4":
                break
            access_resource(choice)
    else:
        print("Authentication failed. Access denied.")

class TestAuthenticate(unittest.TestCase):

    def test_valid_credentials(self):
        """Test authentication with valid credentials."""
        result = authenticate("admin", "password123")
        self.assertTrue(result)

    def test_invalid_password(self):
        """Test authentication with an invalid password."""
        result = authenticate("admin", "wrongpassword")
        self.assertFalse(result)

    def test_invalid_username(self):
        """Test authentication with an invalid username."""
        result = authenticate("wronguser", "password123")
        self.assertFalse(result)

    def test_invalid_username_and_password(self):
        """Test authentication with both invalid username and password."""
        result = authenticate("wronguser", "wrongpassword")
        self.assertFalse(result)

    def test_empty_password(self):
        """Test authentication with an empty password."""
        result = authenticate("admin", "")
        self.assertFalse(result)

    def test_empty_username(self):
        """Test authentication with an empty username."""
        result = authenticate("", "password123")
        self.assertFalse(result)

    def test_empty_username_and_password(self):
        """Test authentication with both empty username and password."""
        result = authenticate("", "")
        self.assertFalse(result)

    def test_valid_username_with_extra_spaces(self):
        """Test authentication with username containing extra spaces."""
        result = authenticate(" admin ", "password123")
        self.assertFalse(result)

    def test_valid_password_with_extra_spaces(self):
        """Test authentication with password containing extra spaces."""
        result = authenticate("admin", " password123 ")
        self.assertFalse(result)

    def test_valid_credentials_with_trailing_spaces(self):
        """Test authentication with trailing spaces in username and password."""
        result = authenticate("admin ", " password123")
        self.assertFalse(result)

# Run the tests
if __name__ == '__main__':
    unittest.main()