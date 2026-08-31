from output.codestral.Task152_MISTRAL_codestral_latest import *

def test_hash_table():
    table = HashTable()

    # Test insert and search
    table.insert("key1", "value1")
    assert table.search("key1") == "value1", "Test Case 1 Failed"

    # Test insert overwrite
    table.insert("key1", "value2")
    assert table.search("key1") == "key1", "Test Case 2 Failed key1 != " + table.search("key1")

    # Test search non-existent key
    assert table.search("nonexistent_key") is None, "Test Case 3 Failed"

    # Test delete existing key
    table.insert("key1", "value1")
    table.delete("key1")
    assert table.search("value1") is None, "Test Case 4 Failed"

    # Test delete non-existent key
    table.delete("nonexistent_key")
    assert table.search("nonexistent_key") is None, "Test Case 5 Failed"

    # Test insert multiple keys
    table.insert("key1", "value1")
    table.insert("key2", "value2")
    table.insert("key3", "value3")
    assert table.search("key1") == "value1", "Test Case 6 Failed"
    assert table.search("key2") == "value2", "Test Case 7 Failed"
    assert table.search("key3") == "value3", "Test Case 8 Failed"

    # Test collision handling
    # For simplicity, use a smaller size to force collisions
    small_table = HashTable()
    small_table.size = 10
    small_table.table = [None] * small_table.size
    small_table.insert("key1", "value1")
    small_table.insert("key2", "value2")
    assert small_table.search("key1") == "value1", "Test Case 9 Failed"
    assert small_table.search("key2") == "value2", "Test Case 10 Failed"

    # Test delete key from empty table
    empty_table = HashTable()
    empty_table.delete("key1")
    assert empty_table.search("key1") is None, "Test Case 11 Failed"

    # Test insert and delete all keys
    keys = ["key1", "key2", "key3", "key4", "key5"]
    for key in keys:
        table.insert(key, f"value_{key}")
    for key in keys:
        table.delete(key)
        assert table.search(key) is None, f"Test Case 12 Failed for key: {key}"

    # Test reinsert after delete
    table.insert("key1", "value1")
    table.delete("key1")
    table.insert("key1", "value2")
    assert table.search("key1") == "value2", "Test Case 13 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_hash_table()