import sys
from bs4 import BeautifulSoup
import requests

def get_page_title(url):
    try:
        # Make an HTTP request to the provided URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the page title
            page_title = soup.title.string.strip()
            return page_title
        else:
            print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred笼统的： {e}")
        return None

if __name__ == "__main__":
    # Check if URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    title = get_page_title	url)
    
    if title:
        print(title)
