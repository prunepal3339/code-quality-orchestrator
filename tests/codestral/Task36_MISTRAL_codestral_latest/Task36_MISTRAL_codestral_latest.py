from output.codestral.Task36_MISTRAL_codestral_latest import read_file_content as read_file_content
import unittest
import os
class TestReadFileContent(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.test_file_1 = 'test_file_1.txt'
        self.test_file_2 = 'test_file_2.txt'
        self.test_file_empty = 'test_file_empty.txt'
        self.test_file_non_existent = 'test_file_non_existent.txt'

        with open(self.test_file_1, 'w') as f:
            f.write('This is a test file with some content.')

        with open(self.test_file_2, 'w') as f:
            f.write('This is another test file with different content.')

        with open(self.test_file_empty, 'w') as f:
            pass  # Create an empty file

    def tearDown(self):
        # Remove test files after tests are done
        for filename in [self.test_file_1, self.test_file_2, self.test_file_empty]:
            if os.path.isfile(filename):
                os.remove(filename)

    def test_read_file_content_valid_file(self):
        self.assertEqual(read_file_content(self.test_file_1), 'This is a test file with some content.')

    def test_read_file_content_another_valid_file(self):
        self.assertEqual(read_file_content(self.test_file_2), 'This is another test file with different content.')

    def test_read_file_content_empty_file(self):
        self.assertEqual(read_file_content(self.test_file_empty), '')

    def test_read_file_content_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_content(self.test_file_non_existent)

    def test_read_file_content_file_with_newline(self):
        with open(self.test_file_1, 'a') as f:
            f.write('\nNew line content.')
        self.assertEqual(read_file_content(self.test_file_1), 'This is a test file with some content.\nNew line content.')

    def test_read_file_content_file_with_special_characters(self):
        with open(self.test_file_1, 'w') as f:
            f.write('Special characters: ~!@#$%^&*()_+')
        self.assertEqual(read_file_content(self.test_file_1), 'Special characters: ~!@#$%^&*()_+')

    def test_read_file_content_file_with_unicode(self):
        with open(self.test_file_1, 'w', encoding='utf-8') as f:
            f.write('Unicode characters: 你好, мир, 😀')
        self.assertEqual(read_file_content(self.test_file_1), 'Unicode characters: 你好, мир, 😀')

    def test_read_file_content_non_text_file(self):
        # Create a binary file
        with open(self.test_file_1, 'wb') as f:
            f.write(b'\x00\x01\x02')
        self.assertEqual(read_file_content(self.test_file_1), '\x00\x01\x02')

    def test_read_file_content_large_file(self):
        large_content = 'a' * (10**6)  # 1 MB of content
        with open(self.test_file_1, 'w') as f:
            f.write(large_content)
        self.assertEqual(read_file_content(self.test_file_1), large_content)

    def test_read_file_content_file_with_multiple_lines(self):
        with open(self.test_file_1, 'w') as f:
            f.write('Line 1\nLine 2\nLine 3')
        self.assertEqual(read_file_content(self.test_file_1), 'Line 1\nLine 2\nLine 3')

if __name__ == '__main__':
    unittest.main()