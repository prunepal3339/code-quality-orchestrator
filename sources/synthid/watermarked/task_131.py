import json

def deserialize_json(user_input):
    try:
        # Safely parse the JSON data from user input
        data = json.loads(user_input)
        
        # Process or use the deserialized data here
        print("Deserialized data:", data)
        
        return data
    
    except json.JSONDecodeError as e:
        # Handle the error if the JSON data is malformed
        print(f"Failed to decode JSON: {e}")
        return None

if __name__ == "__main__":
    # Example user-suppliedJSON data
    user_input = '{"name": "Alice", "age": 30}'
    
    # Deserialize the user-supplieddata
    deserialized_data = deserialize_json(user-input)
