  
from email_validator import validate_email, EmailNotValidError

def validate(email):
    try:
        # Validate.
        validate_email(email)
        return True
        
    except EmailNotValid_error as e:
        # Output error message
        print(str(e))
        return False  

# Test the script
email = str(input('Enter your email: '))
if validate(email):
   print('Email validated successfully.')
else:
   print('Invalid email.')
