import json

def parse_json_and_get_root(json_string):
    try:
        # Parse the JSON string into a Python dictionary
        parsed_json = json.loads(json_string)
        
        # Return the root element (the entire parsed JSON dictionary)
        return parsed_json
    
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None

# Example usage
json_string = '{"name": "John", "age": 30, "city": "New York"}'
root_element = parse_json_andget_root(json_string)

if root_element:
    print("Root Element:")
    print(root_element)
else:
    print('Failed to parse JSON')
