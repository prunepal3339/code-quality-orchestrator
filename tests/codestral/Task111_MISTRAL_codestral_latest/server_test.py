from xmlrpc.client import ServerProxy

def send_request(method_name, *args):
    """Send a request to the XML-RPC server and return the response."""
    try:
        # Connect to the XML-RPC server
        client = ServerProxy("http://192.168.1.148:8000")
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

def test_add_large_numbers():
    response = send_request('add', 1000000, 2000000)
    assert response == 3000000, f"Expected 3000000, got {response}"

def test_add_small_numbers():
    response = send_request('add', 0.1, 0.2)
    assert round(response, 1) == 0.3, f"Expected 0.3, got {response}"

def test_add_negative_and_zero():
    response = send_request('add', -5, 0)
    assert response == -5, f"Expected -5, got {response}"

def test_add_one_negative():
    response = send_request('add', 5, -2)
    assert response == 3, f"Expected 3, got {response}"

def test_add_float_values():
    response = send_request('add', 1.5, 2.5)
    assert response == 4.0, f"Expected 4.0, got {response}"

def test_add_negative_floats():
    response = send_request('add', -1.5, -2.5)
    assert response == -4.0, f"Expected -4.0, got {response}"

# Running all test cases
def run_tests():
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    test_add_zero()
    test_add_large_numbers()
    test_add_small_numbers()
    test_add_negative_and_zero()
    test_add_one_negative()
    test_add_float_values()
    test_add_negative_floats()
    print("All test cases passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()