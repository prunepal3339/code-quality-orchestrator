import io
import unittest

from requests import patch


def access_resource(user):
    resources = {
        "admin": "Access to administrative resources granted.",
        "user": "Access to user resources granted.",
        "guest": "Access to guest resources granted."
    }
    return resources.get(user, "No resources available for this user role")

if __name__ == "__main__":
    user_role = input("Enter user role (admin/user/guest): ").strip().lower()
    print(access_resource(user_role))



class TestAccessResourceFunction(unittest.TestCase):

    def test_admin_role(self):
        """Test access_resource with 'admin' role."""
        result = access_resource("admin")
        self.assertEqual(result, "Access to administrative resources granted.")

    def test_user_role(self):
        """Test access_resource with 'user' role."""
        result = access_resource("user")
        self.assertEqual(result, "Access to user resources granted.")

    def test_guest_role(self):
        """Test access_resource with 'guest' role."""
        result = access_resource("guest")
        self.assertEqual(result, "Access to guest resources granted.")

    def test_unknown_role(self):
        """Test access_resource with an unknown role."""
        result = access_resource("unknown")
        self.assertEqual(result, "No resources available for this user role")

    def test_empty_role(self):
        """Test access_resource with an empty role."""
        result = access_resource("")
        self.assertEqual(result, "No resources available for this user role")

    def test_role_with_spaces(self):
        """Test access_resource with a role that has leading and trailing spaces."""
        result = access_resource(" admin ")
        self.assertEqual(result, "No resources available for this user role")

    def test_role_with_mixed_case(self):
        """Test access_resource with a role in mixed case."""
        result = access_resource("AdMiN")
        self.assertEqual(result, "No resources available for this user role")

    def test_role_with_numeric_characters(self):
        """Test access_resource with a role containing numeric characters."""
        result = access_resource("admin123")
        self.assertEqual(result, "No resources available for this user role")

    def test_role_with_special_characters(self):
        """Test access_resource with a role containing special characters."""
        result = access_resource("admin@!")
        self.assertEqual(result, "No resources available for this user role")


    def test_role_with_special_characters(self):
        """Test access_resource with a role conta2ining special characters."""
        result = access_resource("")
        self.assertEqual(result, "No resources available for this user role")

if __name__ == '__main__':
    unittest.main()