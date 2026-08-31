import requests

class FlaskAppTester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_homepage(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            print("GET request successful.")
            print("Response content:")
            print(response.text)
        else:
            print("GET request failed.")
            print(f"Status code: {response.status_code}")

    def post_user_input(self, user_input):
        response = requests.post(self.base_url, data={'user_input': user_input})
        if response.status_code == 200:
            print("POST request successful.")
            print("Response content:")
            print(response.text)
        else:
            print("POST request failed.")
            print(f"Status code: {response.status_code}")

# Test cases
def run_test_cases():
    base_url = 'http://127.0.0.1:5000/'  # Replace with your Flask app's URL if different
    tester = FlaskAppTester(base_url)

    # Test Case 1: GET request to the homepage
    print("\nTest Case 1: GET request to the homepage")
    tester.get_homepage()

    # Test Case 2: POST request with input 'Hello, World!'
    print("\nTest Case 2: POST request with input 'Hello, World!'")
    tester.post_user_input('Hello, World!')

    # Test Case 3: POST request with empty input
    print("\nTest Case 3: POST request with empty input")
    tester.post_user_input('')

    # Test Case 4: POST request with input containing special characters
    print("\nTest Case 4: POST request with input containing special characters")
    tester.post_user_input('!@#$%^&*()_+')

    # Test Case 5: POST request with a long string
    print("\nTest Case 5: POST request with a long string")
    tester.post_user_input('A' * 1000)

    # Test Case 6: GET request to the homepage after previous POST requests
    print("\nTest Case 6: GET request to the homepage after previous POST requests")
    tester.get_homepage()

    # todo : XSS
    # Test Case 7: POST request with input containing HTML tags
    print("\nTest Case 7: POST request with input containing HTML tags")
    tester.post_user_input('<script>alert("Test")</script>')
    tester.post_user_input('<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>')

    # Test Case 8: POST request with numeric input
    print("\nTest Case 8: POST request with numeric input")
    tester.post_user_input('123456')

    # Test Case 9: POST request with whitespace input
    print("\nTest Case 9: POST request with whitespace input")
    tester.post_user_input('   ')

    # Test Case 10: POST request with a mix of alphanumeric and special characters
    print("\nTest Case 10: POST request with a mix of alphanumeric and special characters")
    tester.post_user_input('Test123!@#')

# Run all test cases
if __name__ == '__main__':
    run_test_cases()
