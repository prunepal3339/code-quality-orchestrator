import hashlib
import os


def signup(username,password):
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  with open("users.txt", "a") as f:
    f.write(f"{username}:{hashed_password}\n")
  print("Signup successful!")

# while True:
#   choice = input("1. Signup\n2. Exit\nEnter choice: ")
#   if choice == "1":
#     signup()
#   elif choice == "2":
#     break
#   else:
#     print("Invalid choice!")



# Test Case 1: Normal Signup
def test_case_1():
  print("Test Case 1: Normal Signup")
  signup("user1", "password123")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("user1:")

# Test Case 2: Signup with Special Characters in Username
def test_case_2():
  print("Test Case 2: Signup with Special Characters in Username")
  signup("user!@#", "password123")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("user!@#:")

# Test Case 3: Signup with Special Characters in Password
def test_case_3():
  print("Test Case 3: Signup with Special Characters in Password")
  signup("user2", "pass!@#123")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("user2:")

# Test Case 4: Signup with Empty Username
def test_case_4():
  print("Test Case 4: Signup with Empty Username")
  signup("", "password123")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith(":")

# Test Case 5: Signup with Empty Password
def test_case_5():
  print("Test Case 5: Signup with Empty Password")
  signup("user3", "")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("user3:")

# Test Case 6: Signup with Long Username and Password
def test_case_6():
  print("Test Case 6: Signup with Long Username and Password")
  long_username = "u" * 100
  long_password = "p" * 100
  signup(long_username, long_password)
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith(long_username + ":")

# Test Case 7: Multiple Users Signup
def test_case_7():
  print("Test Case 7: Multiple Users Signup")
  signup("user4", "password1")
  signup("user5", "password2")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-2].startswith("user4:")
  assert lines[-1].startswith("user5:")

# Test Case 8: Signup with Identical Usernames (should append the new entry)
def test_case_8():
  print("Test Case 8: Signup with Identical Usernames")
  signup("user6", "password3")
  signup("user6", "password4")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-2].startswith("user6:")
  assert lines[-1].startswith("user6:")

# Test Case 9: Signup with Numeric Username and Password
def test_case_9():
  print("Test Case 9: Signup with Numeric Username and Password")
  signup("123456", "654321")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("123456:")

# Test Case 10: Signup with Username and Password Containing Whitespace
def test_case_10():
  print("Test Case 10: Signup with Username and Password Containing Whitespace")
  signup("   ", "   ")
  with open("users.txt", "r") as f:
    lines = f.readlines()
  assert lines[-1].startswith("   :")


if __name__ == "__main__":
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