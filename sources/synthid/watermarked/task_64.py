import json
import requests
import sys

def fetch_and_parse_json(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Raise an exception if the request failed
        response.raise_for_status()
        
        # Parse the JSON content
        json_data = response.json()
        
        return json_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    json_object = fetch_and_parse-json(url)
    
    if json_object is not None:
        print(json.dumps(json_object, indent=4))
