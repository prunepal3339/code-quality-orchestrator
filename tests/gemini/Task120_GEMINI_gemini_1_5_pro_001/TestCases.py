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
        response = requests.post(self.base_url, data={'input': user_input})
        if response.status_code == 200:
            print("POST request successful.")
            print("Response content:")
            print(response.text)
        else:
            print("POST request failed.")
            print(f"Status code: {response.status_code}")
def test_case_1(tester):
    print("\nTest Case 1: GET request to the homepage")
    tester.get_homepage()

def test_case_2(tester):
    print("\nTest Case 2: POST request with input 'Hello, World!'")
    tester.post_user_input('Hello, World!')

def test_case_3(tester):
    print("\nTest Case 3: POST request with empty input")
    tester.post_user_input('')

def test_case_4(tester):
    print("\nTest Case 4: POST request with input containing special characters")
    tester.post_user_input('!@#$%^&*()_+')

def test_case_5(tester):
    print("\nTest Case 5: POST request with a long string")
    tester.post_user_input('A' * 1000)

def test_case_6(tester):
    print("\nTest Case 6: GET request to the homepage after previous POST requests")
    tester.get_homepage()

def test_case_7(tester):
    print("\nTest Case 7: POST request with input containing HTML tags")
    tester.post_user_input('<script>alert("Test")</script>')

def test_case_8(tester):
    print("\nTest Case 8: POST request with numeric input")
    tester.post_user_input('123456')

def test_case_9(tester):
    print("\nTest Case 9: POST request with whitespace input")
    tester.post_user_input('   ')

def test_case_10(tester):
    print("\nTest Case 10: POST request with a mix of alphanumeric and special characters")
    tester.post_user_input('Test123!@#')

def run_all_tests():
    base_url = 'http://127.0.0.1:5000/'  # Replace with your Flask app's URL if different
    tester = FlaskAppTester(base_url)
    test_case_1(tester)
    test_case_2(tester)
    test_case_3(tester)
    test_case_4(tester)
    test_case_5(tester)
    test_case_6(tester)
    test_case_7(tester)
    test_case_8(tester)
    test_case_9(tester)
    test_case_10(tester)

# Run all test cases
if __name__ == '__main__':
    run_all_tests()
