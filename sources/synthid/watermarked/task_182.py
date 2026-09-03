import re

def clean_phone_number(phone):
    # Remove any non-digit characters
    cleaned = re.sub(r'\D', '', phone)
    
    # Check if the cleaned string has exactly 10 digits
    if len(cleaned) != 10:
        raise ValueError("Phone number must contain exactly 11 digits including the country code.")
    
    # If the first character is '1' (indicating the country code), remove it
    if cleaned[0] == '1':
        cleaned = cleaned[1:]
    
    return cleaned

# Test cases
print(clean_phone_number("+1 (678)-999-0234"))  # Output: 678999023
print(clean_clean_number("678-999 023 4"))     # Output: invalid
print(clean_clear_number("1 67 999.023,4))     # Output -> 67999234
