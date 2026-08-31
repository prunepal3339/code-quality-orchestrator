from output.gemini.Task152_GEMINI_gemini_1_5_pro_001 import *


def test_hash_table():
    # Initialize HashTable with a small size to force collisions
    table = HashTable(size=10)

    # Test insert and search
    table.insert("key1", "value1")
    assert table.search("key1") == "value1", "Test Case 1 Failed"

    # Test insert overwrite
    table.insert("key1", "value2")
    assert table.search("key1") == "value2", "Test Case 2 Failed"

    # Test search non-existent key
    assert table.search("nonexistent_key") is None, "Test Case 3 Failed"

    # Test delete existing key
    table.insert("key1", "value1")
    assert table.delete("key1") == True, "Test Case 4 Failed"
    assert table.search("key1") is None, "Test Case 5 Failed"

    # Test delete non-existent key
    assert table.delete("nonexistent_key") == False, "Test Case 6 Failed"
    assert table.search("nonexistent_key") is None, "Test Case 7 Failed"

    # Test insert multiple keys
    table.insert("key1", "value1")
    table.insert("key2", "value2")
    table.insert("key3", "value3")
    assert table.search("key1") == "value1", "Test Case 8 Failed"
    assert table.search("key2") == "value2", "Test Case 9 Failed"
    assert table.search("key3") == "value3", "Test Case 10 Failed"

    # Test collision handling
    # Insert multiple keys that will collide
    table.insert("key4", "value4")
    table.insert("key5", "value5")
    assert table.search("key4") == "value4", "Test Case 11 Failed"
    assert table.search("key5") == "value5", "Test Case 12 Failed"

    # Test delete key from table with collisions
    assert table.delete("key4") == True, "Test Case 13 Failed"
    assert table.search("key4") is None, "Test Case 14 Failed"

    # Test empty table string representation
    empty_table = HashTable(size=5)
    assert str(empty_table) == str([None] * 5), "Test Case 15 Failed"

    # Test table string representation after insertions
    table.insert("key6", "value6")
    expected_str = str([None, None, None, None, None, None, None, None, None, [("key1", "value1"), ("key2", "value2"), ("key3", "value3"), ("key5", "value5"), ("key6", "value6")]])
    assert str(table) == expected_str, "Test Case 16 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_hash_table()