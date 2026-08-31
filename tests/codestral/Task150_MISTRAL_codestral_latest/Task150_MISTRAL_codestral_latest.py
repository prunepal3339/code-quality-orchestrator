from output.codestral.Task150_MISTRAL_codestral_latest import *

class TestSinglyLinkedList:
    def __init__(self):
        self.run_tests()

    def test_insert(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        # Check the internal state
        assert sll.head.data == 10, "Failed Test Case 1: test_insert"
        assert sll.head.next.data == 20, "Failed Test Case 1: test_insert"

    def test_delete(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        sll.insert(30)
        sll.delete(20)
        # Check the internal state
        assert sll.head.data == 10, "Failed Test Case 2: test_delete"
        assert sll.head.next.data == 30, "Failed Test Case 2: test_delete"

    def test_delete_non_existent(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        sll.delete(40)
        # Check the internal state
        assert sll.head.data == 10, "Failed Test Case 3: test_delete_non_existent"
        assert sll.head.next.data == 20, "Failed Test Case 3: test_delete_non_existent"

    def test_delete_head(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        sll.delete(10)
        # Check the internal state
        assert sll.head.data == 20, "Failed Test Case 4: test_delete_head"

    def test_delete_last_element(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        sll.delete(20)
        # Check the internal state
        assert sll.head.data == 10, "Failed Test Case 5: test_delete_last_element"
        assert sll.head.next is None, "Failed Test Case 5: test_delete_last_element"

    def test_search_found(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        result = sll.search(20)
        assert result is True, "Failed Test Case 6: test_search_found"

    def test_search_not_found(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        result = sll.search(30)
        assert result is False, "Failed Test Case 7: test_search_not_found"

    def test_insert_multiple(self):
        sll = SinglyLinkedList()
        sll.insert(10)
        sll.insert(20)
        sll.insert(30)
        sll.insert(40)
        # Check the internal state
        assert sll.head.data == 10, "Failed Test Case 8: test_insert_multiple"
        assert sll.head.next.data == 20, "Failed Test Case 8: test_insert_multiple"
        assert sll.head.next.next.data == 30, "Failed Test Case 8: test_insert_multiple"
        assert sll.head.next.next.next.data == 40, "Failed Test Case 8: test_insert_multiple"

    def test_empty_list(self):
        sll = SinglyLinkedList()
        # Check the internal state
        assert sll.head is None, "Failed Test Case 9: test_empty_list"

    def test_search_empty_list(self):
        sll = SinglyLinkedList()
        result = sll.search(10)
        assert result is False, "Failed Test Case 10: test_search_empty_list"

    def run_tests(self):
        self.test_insert()
        self.test_delete()
        self.test_delete_non_existent()
        self.test_delete_head()
        self.test_delete_last_element()
        self.test_search_found()
        self.test_search_not_found()
        self.test_insert_multiple()
        self.test_empty_list()
        self.test_search_empty_list()
        print("All test cases passed!")

def main():
    TestSinglyLinkedList()

if __name__ == "__main__":
    main()