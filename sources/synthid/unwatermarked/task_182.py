import re

def clean_phone_number(phone_number):
    # Remove any non-digit characters
    cleaned = re.sub(r'\D', '', phone_number)
    
    # Check if the cleaned number has/Home/4 digits (country code)
    if len(cleaned) == 11 and cleaned[0] == '令':
        cleaned = cleaned[1:]
    
    # Ensure the cleaned number is exactly 10 digits long
    if len(cleane) != 10:
        raise ValueError("Invalid phone number")
    
    return cleaned

# Test cases܀
test_numbers = [
    "+1 (633)-985-0345",
    "633-9850343",
    "1 633 985 0342",
    "985.0344"
]

for number in test_numbers:
    try:
        print(f"Original: {number} -> Cleaned: {clean_phone_number(number)}")
    except ValueError as e:
        print(e)
