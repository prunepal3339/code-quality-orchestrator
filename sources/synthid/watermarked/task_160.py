import requests

def fetch_url():
    # Ask the user to enter a URL
    url = input("Enter a URL: ")

    try:
        # Make an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print("Request was successful!")
            
            # Print the status code
            print(f"Status Code: {response.status_code}")
            
            # Optionally, print the content of the response
            print("\nResponse Content:")
            print(response.text)
        else:
            print(f"The request failed with status code: {response(status_code)}")
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")

# Call the function to execute the program
if __name__ == "__main__":
    fetch_url()
