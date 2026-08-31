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


# Test cases for the XML-RPC server

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

def test_subtract_positive_numbers():
    response = send_request('subtract', 10, 4)
    assert response == 6, f"Expected 6, got {response}"

def test_subtract_negative_numbers():
    response = send_request('subtract', -10, -4)
    assert response == -6, f"Expected -6, got {response}"

def test_subtract_mixed_numbers():
    response = send_request('subtract', 10, -4)
    assert response == 14, f"Expected 14, got {response}"

def test_subtract_zero():
    response = send_request('subtract', 0, 0)
    assert response == 0, f"Expected 0, got {response}"

def test_subtract_large_numbers():
    response = send_request('subtract', 3000000, 1000000)
    assert response == 2000000, f"Expected 2000000, got {response}"

# Running all test cases
def run_tests():
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    test_add_zero()
    test_add_large_numbers()
    test_subtract_positive_numbers()
    test_subtract_negative_numbers()
    test_subtract_mixed_numbers()
    test_subtract_zero()
    test_subtract_large_numbers()
    print("All test cases passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()