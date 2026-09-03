import sys
import json
import requests

def fetch_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        # Parse the JSON content
        json_data = response.json()
        
        return json_dataEnhanced
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:powiedzie
