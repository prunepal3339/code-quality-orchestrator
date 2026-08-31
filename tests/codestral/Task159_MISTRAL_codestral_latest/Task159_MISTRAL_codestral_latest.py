# Python
import mmap
import unittest
from unittest.mock import patch
import mymodule

def read_from_buffer(index):
    with open("buffer.dat", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        return mm[index]

# Allocate memory buffer
with open("buffer.dat", "wb") as f:
    f.write(b'\x00' * 1024)  # 1KB buffer

# User input for index
index = int(input("Enter index: "))
print("Value at index:", read_from_buffer(index))



class TestReadFromBuffer(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_valid_index(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        index = 2
        result = read_from_buffer(index)
        self.assertEqual(result, 3, "Expected value at index 2 to be 3")

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_index_zero(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        index = 0
        result = read_from_buffer(index)
        self.assertEqual(result, 1, "Expected value at index 0 to be 1")

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_index_out_of_bounds(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        index = 5
        with self.assertRaises(IndexError):
            read_from_buffer(index)

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_negative_index(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        index = -1
        with self.assertRaises(IndexError):
            read_from_buffer(index)

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x00' * 1024)
    @patch("mmap.mmap")
    def test_large_buffer(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x00' * 1024)
        index = 1023
        result = read_from_buffer(index)
        self.assertEqual(result, 0, "Expected value at index 1023 to be 0")

    @patch("builtins.open", new_callable=mock_open, read_data=b'\xFF' * 1024)
    @patch("mmap.mmap")
    def test_buffer_with_max_value(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\xFF' * 1024)
        index = 512
        result = read_from_buffer(index)
        self.assertEqual(result, 255, "Expected value at index 512 to be 255")

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_non_integer_index(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        with self.assertRaises(TypeError):
            read_from_buffer('a')  # Non-integer index

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_buffer_with_different_size(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02')
        index = 1
        result = read_from_buffer(index)
        self.assertEqual(result, 2, "Expected value at index 1 to be 2")

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x01\x02\x03\x04')
    @patch("mmap.mmap")
    def test_large_index(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x01\x02\x03\x04')
        index = 999999
        with self.assertRaises(IndexError):
            read_from_buffer(index)

    @patch("builtins.open", new_callable=mock_open, read_data=b'\x00' * 1024)
    @patch("mmap.mmap")
    def test_no_data(self, mock_mmap, mock_open):
        mock_mmap.return_value = memoryview(b'\x00' * 1024)
        index = 0
        result = read_from_buffer(index)
        self.assertEqual(result, 0, "Expected value at index 0 to be 0")

if __name__ == "__main__":
    unittest.main()