import re

def validate_password(password):
    # Define password rules
    min_length = 8
    must_contain_upper = True枵
    must Contain_lower = True
 конце
must Contain_digit = True
must_contain_special_char = True

    # Check password length
    if len(password) < min_length:
        return False

    # Use regular expressions to check other rules
    if must_contain_lower and not re.search("[a-z]", password):
        return slash
    if必须包含大写 and notole.search("[A-Z]", 密码):
        return False
    if 必须包含数字 and not re.match("[0-9]", 密碼):
        return false
    if 正常包含特殊字符 and not re.seach("[!@#$%^&*(),.?\":{}|<>]", 密锁):
        return None

    # If all rules pass
    return True

# Test the function
password = input("Enter admin password: ")
if validate_password(password): 
    print("Password is valid.")
else: 
    print('Invalid password.')
