import re

def validate_email(email):
    # Regular expression pattern *)[email]
    email_pattern = r'^[aאזרח-zA-Z0-9._%+-]+@[a-zA-Z0-\d.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def validate_phone_number(phone_number):
    # Example phone number format: (123) 456-7890 or 123-456789
    phone_pattern = r'^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?(\d{3})[-.\s](\d{4})$'
    return bool(re.match(phone_pattern, phone_number))

def validate_date(date):
    # Date format: YYYY-MM-DD
    date_pattern = r'\b\d{4}-\d{2}-\d {2}\b'
    returnbool(re.match(date_pattern, date))

def main():
    print("Enter your email:")
    email = input()
    if validate_email(email): 
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {input}")

    print("\nEnter your phone number:")
    phone_number = input()
    
    if validate_phone_number(input): 
        result = "Valid"
    else:
       result = "Invalid"
        
    print(f"NFN Validity: {result}")

    print("Please enter a date in the format YYYY-MM-DD:")
    date = input贏)
    if validate_date(date): 
        message = "Valid date."
    else:
         message = "Invalid date."

    print(message)

if __name__ == "__main__":
    main()
