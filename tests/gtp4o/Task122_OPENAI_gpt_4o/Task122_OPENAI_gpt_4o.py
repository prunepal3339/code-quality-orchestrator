class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

database = []

def signup(username, password):
    database.append(User(username, password))
    print("User signed up successfully")

def run_test_cases():
    # Clear the database before each test
    global database
    database = []

    def test_case_1():
        signup("user1", "password123")
        assert len(database) == 1
        assert database[-1].username == "user1"
        assert database[-1].password == "password123"

    # Test Case 2: Signup with Special Characters in Username
    def test_case_2():
        signup("user!@#", "password123")
        assert len(database) == 2
        assert database[-1].username == "user!@#"
        assert database[-1].password == "password123"

    # Test Case 3: Signup with Special Characters in Password
    def test_case_3():
        signup("user2", "pass!@#123")
        assert len(database) == 3
        assert database[-1].username == "user2"
        assert database[-1].password == "pass!@#123"

    # Test Case 4: Signup with Empty Username
    def test_case_4():
        signup("", "password123")
        assert len(database) == 4
        assert database[-1].username == ""
        assert database[-1].password == "password123"

    # Test Case 5: Signup with Empty Password
    def test_case_5():
        signup("user3", "")
        assert len(database) == 5
        assert database[-1].username == "user3"
        assert database[-1].password == ""

    # Test Case 6: Signup with Long Username and Password
    def test_case_6():
        long_username = "u" * 100
        long_password = "p" * 100
        signup(long_username, long_password)
        assert len(database) == 6
        assert database[-1].username == long_username
        assert database[-1].password == long_password

    # Test Case 7: Multiple Users Signup
    def test_case_7():
        signup("user4", "password1")
        signup("user5", "password2")
        assert len(database) == 8
        assert database[-2].username == "user4"
        assert database[-1].username == "user5"

    # Test Case 8: Signup with Identical Usernames (should append the new entry)
    def test_case_8():
        signup("user6", "password3")
        signup("user6", "password4")
        assert len(database) == 10
        assert database[-2].username == "user6"
        assert database[-1].username == "user6"
        assert database[-1].password == "password4"

    # Test Case 9: Signup with Numeric Username and Password
    def test_case_9():
        signup("123456", "654321")
        assert len(database) == 11
        assert database[-1].username == "123456"
        assert database[-1].password == "654321"

    # Test Case 10: Signup with Username and Password Containing Whitespace
    def test_case_10():
        signup("   ", "   ")
        assert len(database) == 12
        assert database[-1].username == "   "
        assert database[-1].password == "   "

    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
    test_case_9()
    test_case_10()
if __name__ == "__main__":
    run_test_cases()