
import hashlib
import os

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def signup(username,password):
    hashed_password = hash_password(password)
    with open("passwords.txt", "ab") as file:
        file.write(username.encode('utf-8') + b":" + hashed_password + b"\\n")
    print("Signup successful!")


def run_test_cases():
    # Cleanup passwords.txt if it exists
    if os.path.exists("passwords.txt"):
        os.remove("passwords.txt")

    # Test Case 1: Normal Signup
    def test_case_1():
        print("Test Case 1: Normal Signup")
        signup('user1', 'password123')

    # Test Case 2: Signup with Special Characters in Username
    def test_case_2():
        print("Test Case 2: Signup with Special Characters in Username")
        signup('user!@#', 'password123')

    # Test Case 3: Signup with Special Characters in Password
    def test_case_3():
        print("Test Case 3: Signup with Special Characters in Password")
        signup('user2', 'pass!@#123')

    # Test Case 4: Signup with Empty Username
    def test_case_4():
        print("Test Case 4: Signup with Empty Username")
        signup('', 'password123')

    # Test Case 5: Signup with Empty Password
    def test_case_5():
        print("Test Case 5: Signup with Empty Password")
        signup('user3', '')

    # Test Case 6: Signup with Long Username and Password
    def test_case_6():
        print("Test Case 6: Signup with Long Username and Password")
        signup('u' * 100, 'p' * 100)

    # Test Case 7: Signup with Multiple Users
    def test_case_7():
        print("Test Case 7: Signup with Multiple Users")
        signup('user4', 'password1')
        signup('user5', 'password2')

    # Test Case 8: Signup with Identical Usernames
    def test_case_8():
        print("Test Case 8: Signup with Identical Usernames")
        signup('user6', 'password3')
        signup('user6', 'password4')

    # Test Case 9: File Handling Test
    def test_case_9():
        print("Test Case 9: File Handling Test")
        signup('user7', 'password5')

    # Test Case 10: Invalid Characters in Username and Password
    def test_case_10():
        print("Test Case 10: Invalid Characters in Username and Password")
        signup('user\x00', 'password\x00')

    # Test Case 11: Duplicate Entries
    def test_case_11():
        print("Test Case 11: Duplicate Entries")
        signup('user8', 'password6')
        signup('user8', 'password6')

    # Test Case 12: Large Data
    def test_case_12():
        print("Test Case 12: Large Data")
        long_username = 'u' * 1000
        long_password = 'p' * 1000
        signup(long_username, long_password)

    # Test Case 13: File Size Limits
    def test_case_13():
        print("Test Case 13: File Size Limits")
        for i in range(100):
            signup(f'user{i}', 'password123')

    # Test Case 14: Encoding Issues
    def test_case_14():
        print("Test Case 14: Encoding Issues")
        signup('user9', 'password123')
        # Simulate different encoding issues by writing non-utf-8 data
        with open("passwords.txt", "ab") as file:
            file.write(b'\x80\x81\x82\x83')

    def test_case_17():
        print("Test Case 17: Handling Multiple Extensions")
        signup('user.with.many.extensions', 'password')

    # Test Case 18: Security Measures
    def test_case_18():
        print("Test Case 18: Security Measures")
        # Test that the hashed password is not directly readable
        signup('user11', 'password11')
        with open("passwords.txt", "rb") as file:
            content = file.read()
        assert b'password11' not in content

    # Test Case 19: Exception Handling
    def test_case_19():
        print("Test Case 19: Exception Handling")
        try:
            # This will fail if the file path is incorrect or permissions are wrong
            signup('user12', 'password12')
        except Exception as e:
            print(f"Exception occurred: {e}")

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
    test_case_11()
    test_case_12()
    test_case_13()
    test_case_14()
    test_case_17()
    test_case_18()
    test_case_19()

if __name__ == "__main__":
    run_test_cases()