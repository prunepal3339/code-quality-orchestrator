from xmlrpc.client import ServerProxy

def send_request(method_name, *args):
    """Send a request to the XML-RPC server and return the response."""
    try:
        # Connect to the XML-RPC server
        client = ServerProxy("http://192.168.1.148:8001")
        # Call the specified method with arguments
        result = getattr(client, method_name)(*args)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def test_add_positive_numbers():
    response = send_request('add', 5, 3)
    assert response == 8, f"Expected 8, got {response}"

def test_add_negative_numbers():
    response = send_request('add', -5, -3)
    assert response == -8, f"Expected -8, got {response}"

def test_add_mixed_numbers():
    response = send_request('add', 5, -3)
    assert response == 2, f"Expected 2, got {response}"

def test_add_zero():
    response = send_request('add', 0, 0)
    assert response == 0, f"Expected 0, got {response}"

def test_pow_positive_numbers():
    response = send_request('pow', 2, 3)
    assert response == 8, f"Expected 8, got {response}"

def test_pow_zero_exponent():
    response = send_request('pow', 5, 0)
    assert response == 1, f"Expected 1, got {response}"

def test_pow_negative_exponent():
    response = send_request('pow', 2, -2)
    assert response == 0.25, f"Expected 0.25, got {response}"

def test_sum_list_of_numbers():
    response = send_request('sum', [1, 2, 3, 4])
    assert response == 10, f"Expected 10, got {response}"

def test_sum_empty_list():
    response = send_request('sum', [])
    assert response == 0, f"Expected 0, got {response}"

def test_sum_negative_numbers():
    response = send_request('sum', [-1, -2, -3, -4])
    assert response == -10, f"Expected -10, got {response}"

# Running all test cases
def run_tests():
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    test_add_zero()
    test_pow_positive_numbers()
    test_pow_zero_exponent()
    test_pow_negative_exponent()
    test_sum_list_of_numbers()
    test_sum_empty_list()
    test_sum_negative_numbers()
    print("All test cases passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()