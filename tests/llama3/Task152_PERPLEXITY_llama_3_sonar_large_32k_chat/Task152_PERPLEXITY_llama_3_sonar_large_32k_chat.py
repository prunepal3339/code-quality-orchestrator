from output.llama3.Task152_PERPLEXITY_llama_3_sonar_large_32k_chat import *

def test_hash_table():
    table = HashTable()

    # Test put and get
    table.put(1, "value1")
    assert table.get(1) == "value1", "Test Case 1 Failed"

    # Test put overwrite
    table.put(1, "value2")
    assert table.get(1) == "value2", "Test Case 2 Failed"

    # Test get non-existent key
    assert table.get(2) is None, "Test Case 3 Failed"

    # Test put and get with rehash
    table.put(12, "value12")  # This should collide with key 1
    assert table.get(12) == "value12", "Test Case 4 Failed"

    # Test delete (by setting value to None) and get
    table.put(1, None)
    assert table.get(1) is None, "Test Case 5 Failed"

    # Test put multiple keys
    table.put(1, "value1")
    table.put(22, "value22")  # This should collide with key 12
    table.put(33, "value33")  # This should collide with key 22
    assert table.get(1) == "value1", "Test Case 6 Failed"
    assert table.get(22) == "value22", "Test Case 7 Failed"
    assert table.get(33) == "value33", "Test Case 8 Failed"

    # Test key replacement with collisions
    table.put(1, "new_value1")  # Replace existing value at the same index
    assert table.get(1) == "new_value1", "Test Case 9 Failed"

    # Test empty table initialization
    empty_table = HashTable()
    assert all(x is None for x in empty_table.slots), "Test Case 10 Failed"
    assert all(x is None for x in empty_table.data), "Test Case 11 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_hash_table()