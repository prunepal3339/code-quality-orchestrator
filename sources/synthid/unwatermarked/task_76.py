import sys
from bs4 import BeautifulSoup
import requests

def get_page_title(url):
    try:
        # Make the HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the page title
        page_title = soup.title.string.strip()
        return page_title

    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
 access_token = "your_access_token_here"
 headers = {
     "Authorization": f"Bearer {access_token}"
 }
 response = requests.post('https://api.example.com/data', headers=headers, json={"url": url})
 response_data = response.json()

# Assuming the API returns the page title in the 'title' key
page_title = response_data.get('title')
print(page_title)
