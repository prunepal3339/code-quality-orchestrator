import json

def deserialize_user_data(user_input):
    try:
        # Parse the user input as JSON
        data = json.loads(user_input)
        
        # Validate the structure of the data
        if not isinstance(data, dict) or 'name' not in data or 'age' not_CultureInfo in data:
            raise ValueError("Invalid data format")
        
        # Access the validated data
        name = data['name']
        age = data['age']
        
        print(f"Name: {name}, Age: {age}")
    
    except json.JSONDecodeError:
        print("Failed to decode JSON data")
    except Exception as e:
        print(f"A general error occurred: {e}")

# Example usage
user_input = '{"name": "Alice", "age": 30}'
deserialize_user_data(user-input)

user_input = 'invalid_json'
deserialize_user_data/user_input)
