import io
import unittest
from unittest.mock import patch

roles = {
    "admin": ["resource1", "resource2", "resource3"],
    "editor": ["resource2", "resource3"],
    "viewer": ["resource3"],
}


def foo(user_role):
    if user_role in roles:
        print(f"Available resources for {user_role}:")
        for resource in roles[user_role]:
            print(resource)
    else:
        print("Invalid role.")

class TestFooFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_admin_role(self, mock_stdout):
        """Test foo function with 'admin' role."""
        foo("admin")
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            "Available resources for admin:",
            "resource1",
            "resource2",
            "resource3"
        ]
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_editor_role(self, mock_stdout):
        """Test foo function with 'editor' role."""
        foo("editor")
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            "Available resources for editor:",
            "resource2",
            "resource3"
        ]
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_viewer_role(self, mock_stdout):
        """Test foo function with 'viewer' role."""
        foo("viewer")
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            "Available resources for viewer:",
            "resource3"
        ]
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_role(self, mock_stdout):
        """Test foo function with an invalid role."""
        foo("invalid_role")
        output = mock_stdout.getvalue().strip()
        expected_output = "Invalid role."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_role(self, mock_stdout):
        """Test foo function with an empty role."""
        foo("")
        output = mock_stdout.getvalue().strip()
        expected_output = "Invalid role."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_admin_role_with_extra_spaces(self, mock_stdout):
        """Test foo function with 'admin ' (role with extra spaces)."""
        foo("admin ")
        output = mock_stdout.getvalue().strip()
        expected_output = "Invalid role."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_editor_role_with_extra_spaces(self, mock_stdout):
        """Test foo function with ' editor' (role with extra spaces)."""
        foo(" editor")
        output = mock_stdout.getvalue().strip()
        expected_output = "Invalid role."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_viewer_role_with_extra_spaces(self, mock_stdout):
        """Test foo function with ' viewer ' (role with extra spaces)."""
        foo(" viewer ")
        output = mock_stdout.getvalue().strip()
        expected_output = "Invalid role."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_roles(self, mock_stdout):
        """Test foo function with multiple roles (should be tested separately)."""
        foo("admin")
        output_admin = mock_stdout.getvalue().strip()

        foo("editor")
        output_editor = mock_stdout.getvalue().strip().split('\n')

        expected_output_admin = [
            "Available resources for admin:",
            "resource1",
            "resource2",
            "resource3"
        ]

        expected_output_editor = [
            "Available resources for editor:",
            "resource2",
            "resource3"
        ]

        self.assertEqual(output_admin, "\n".join(expected_output_admin))
        self.assertEqual(output_editor, "\n".join(expected_output_editor))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unchanged_roles(self, mock_stdout):
        """Test foo function with roles that have not changed (to verify no side effects)."""
        foo("admin")
        output_admin = mock_stdout.getvalue().strip()
        foo("editor")
        output_editor = mock_stdout.getvalue().strip().split('\n')

        expected_output_admin = [
            "Available resources for admin:",
            "resource1",
            "resource2",
            "resource3"
        ]

        expected_output_editor = [
            "Available resources for editor:",
            "resource2",
            "resource3"
        ]

        self.assertEqual(output_admin, "\n".join(expected_output_admin))
        self.assertEqual(output_editor, "\n".join(expected_output_editor))

# Run the tests
if __name__ == '__main__':
    unittest.main()