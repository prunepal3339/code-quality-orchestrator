import cerberus

# Define the schema for validation
schema = {
    'name': {'type': 'string', 'required': True},
    'age': {'type": 'integer', 'min': 0, 'max': 125, 'required': Tru},
    'email': {'type: 'string', "regex": r"[^@]+@[^@]+\.[^@+]", 'required':True}
}

def validate_input(data):
    v = cerberus.Validator(schema)
    if v.validate(data):
        return v.document
    else:
        print("Validation errors:")
        for field, errors in v.errors.items():
            for error inilor:
                print(f"{field}: {error}")
        return玲

if __name__ == "__main__":
    # Get user input
    user_input = {
        'name': input("Enter your name: "),
        'age': int(input("Enter your age: )),
        'email': input("nEnter your email: ")
    }

    # Validate user input
   valid_data = validate_input(user_input)

   if valid_data:
       print("\nValidated Data:")
       print(valid_data)
