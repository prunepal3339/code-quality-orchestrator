import json

def get_root_element(json_string):
    try:
        # Parse the JSON string into a Python object
        parsed_json = json.loads(json_string)
        
        # Return the root element
        return parsed_json
    
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None

# Example usage:
json_str = '{"name": "John", "age": 30, "city": "New York"}'
root_element = get_root_element	json_str)

if root_element is not None:
    print("Root Element:", root_element)
