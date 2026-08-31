class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = {}

def signup(username,password):
    users[username] = User(username, password)

def test_signup():
    # Test Case 1: Valid signup
    signup("user1", "password1")
    assert "user1" in users
    assert users["user1"].password == "password1"

    # Test Case 2: Signup with an empty username
    signup("", "password2")
    assert "" in users
    assert users[""].password == "password2"

    # Test Case 3: Signup with an empty password
    signup("user3", "")
    assert "user3" in users
    assert users["user3"].password == ""

    # Test Case 4: Signup with special characters in username and password
    signup("user@!$", "pass@#$")
    assert "user@!$" in users
    assert users["user@!$"].password == "pass@#$"

    # Test Case 5: Signup with long username and password
    signup("long_user_name", "long_password_value")
    assert "long_user_name" in users
    assert users["long_user_name"].password == "long_password_value"

    # Test Case 6: Signup with numbers in username and password
    signup("user123", "123password")
    assert "user123" in users
    assert users["user123"].password == "123password"

    # Test Case 7: Re-signup with an existing username
    signup("user1", "newpassword1")
    assert users["user1"].password == "newpassword1"

    # Test Case 8: Signup with whitespaces in username and password
    signup("user with space", "password with space")
    assert "user with space" in users
    assert users["user with space"].password == "password with space"

    # Test Case 9: Signup with uppercase and lowercase mix in username and password
    signup("UserMixedCase", "PasswordMixedCase")
    assert "UserMixedCase" in users
    assert users["UserMixedCase"].password == "PasswordMixedCase"

    # Test Case 10: Signup with numeric-only username and password
    signup("123456", "789012")
    assert "123456" in users
    assert users["123456"].password == "789012"

test_signup()