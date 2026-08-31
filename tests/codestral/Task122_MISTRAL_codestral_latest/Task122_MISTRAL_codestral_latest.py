# Python
passwords = {}

def signup(username, password):
    passwords[username] = password

# Test cases
def run_test_cases():
    # Cleanup the passwords dictionary
    global passwords
    passwords = {}

    # Test Case 1: Normal Signup
    def test_case_1():
        print("Test Case 1: Normal Signup")
        signup('user1', 'password123')
        assert passwords['user1'] == 'password123'

    # Test Case 2: Signup with Special Characters in Username
    def test_case_2():
        print("Test Case 2: Signup with Special Characters in Username")
        signup('user!@#', 'password123')
        assert passwords['user!@#'] == 'password123'

    # Test Case 3: Signup with Special Characters in Password
    def test_case_3():
        print("Test Case 3: Signup with Special Characters in Password")
        signup('user2', 'pass!@#123')
        assert passwords['user2'] == 'pass!@#123'

    # Test Case 4: Signup with Empty Username
    def test_case_4():
        print("Test Case 4: Signup with Empty Username")
        signup('', 'password123')
        assert passwords[''] == 'password123'

    # Test Case 5: Signup with Empty Password
    def test_case_5():
        print("Test Case 5: Signup with Empty Password")
        signup('user3', '')
        assert passwords['user3'] == ''

    # Test Case 6: Signup with Long Username and Password
    def test_case_6():
        print("Test Case 6: Signup with Long Username and Password")
        long_username = 'u' * 100
        long_password = 'p' * 100
        signup(long_username, long_password)
        assert passwords[long_username] == long_password

    # Test Case 7: Signup with Multiple Users
    def test_case_7():
        print("Test Case 7: Signup with Multiple Users")
        signup('user4', 'password1')
        signup('user5', 'password2')
        assert passwords['user4'] == 'password1'
        assert passwords['user5'] == 'password2'

    # Test Case 8: Signup with Identical Usernames
    def test_case_8():
        print("Test Case 8: Signup with Identical Usernames")
        signup('user6', 'password3')
        signup('user6', 'password4')  # This should overwrite the previous password
        assert passwords['user6'] == 'password4'

    # Test Case 9: Signup with Numeric Username and Password
    def test_case_9():
        print("Test Case 9: Signup with Numeric Username and Password")
        signup('123456', '654321')
        assert passwords['123456'] == '654321'

    # Test Case 10: Signup with Whitespace Username and Password
    def test_case_10():
        print("Test Case 10: Signup with Whitespace Username and Password")
        signup('   ', '   ')
        assert passwords['   '] == '   '

    # Run all test cases
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