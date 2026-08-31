from output.gtp4o.Task152_OPENAI_gpt_4o import *



def test_hash_table():
    table = HashTable()

    # Test insert and search
    table.insert(1, "value1")
    assert table.search(1) == "value1", "Test Case 1 Failed"

    # Test insert overwrite
    table.insert(1, "value2")
    assert table.search(1) == "value2", "Test Case 2 Failed"

    # Test search non-existent key
    assert table.search(2) is None, "Test Case 3 Failed"

    # Test delete existing key
    table.insert(1, "value1")
    table.delete(1)
    assert table.search(1) is None, "Test Case 4 Failed"

    # Test delete non-existent key
    table.delete(2)
    assert table.search(2) is None, "Test Case 5 Failed"

    # Test insert multiple keys
    table.insert(1, "value1")
    table.insert(11, "value11")  # Collides with index 1
    table.insert(21, "value21")  # Collides with index 1
    assert table.search(1) == "value1", "Test Case 6 Failed"
    assert table.search(11) == "value11", "Test Case 7 Failed"
    assert table.search(21) == "value21", "Test Case 8 Failed"

    # Test collisions handling (overwrite at the same index)
    table.insert(1, "new_value1")  # Overwrites previous value at index 1
    assert table.search(1) == "new_value1", "Test Case 9 Failed"

    # Test empty table
    empty_table = HashTable()
    assert all(x is None for x in empty_table.table), "Test Case 10 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_hash_table()