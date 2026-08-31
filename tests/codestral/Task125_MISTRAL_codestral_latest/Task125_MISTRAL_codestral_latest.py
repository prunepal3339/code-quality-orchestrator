# Python
import io
import unittest
from unittest.mock import patch

resources = {
    'A': 'Resource A',
    'B': 'Resource B',
    'C': 'Resource C'
}


def access_resource(user_input):
    if user_input in resources:
        print(f'Access granted to: {resources[user_input]}')
    else:
        print('Access denied. Invalid key.')



class TestResourceAccess(unittest.TestCase):

    @patch('builtins.input', side_effect=['A'])
    @patch('builtins.print')
    def test_valid_key_A(self, mock_print, mock_input):
        """Test access with a valid key 'A'."""
        access_resource('A')
        mock_print.assert_called_once_with('Access granted to: Resource A')

    @patch('builtins.input', side_effect=['B'])
    @patch('builtins.print')
    def test_valid_key_B(self, mock_print, mock_input):
        """Test access with a valid key 'B'."""
        access_resource('B')
        mock_print.assert_called_once_with('Access granted to: Resource B')

    @patch('builtins.input', side_effect=['C'])
    @patch('builtins.print')
    def test_valid_key_C(self, mock_print, mock_input):
        """Test access with a valid key 'C'."""
        access_resource('C')
        mock_print.assert_called_once_with('Access granted to: Resource C')

    @patch('builtins.input', side_effect=['D'])
    @patch('builtins.print')
    def test_invalid_key(self, mock_print, mock_input):
        """Test access with an invalid key 'D'."""
        access_resource('D')
        mock_print.assert_called_once_with('Access denied. Invalid key.')

    @patch('builtins.input', side_effect=[''])
    @patch('builtins.print')
    def test_empty_key(self, mock_print, mock_input):
        """Test access with an empty key."""
        access_resource('')
        mock_print.assert_called_once_with('Access denied. Invalid key.')

    @patch('builtins.input', side_effect=['A'])
    def test_print_called_correctly(self, mock_input):
        """Test that print is called once with the correct message for valid key 'A'."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            access_resource('A')
            self.assertEqual(fake_out.getvalue().strip(), 'Access granted to: Resource A')

    @patch('builtins.input', side_effect=['B'])
    def test_print_called_correctly_for_B(self, mock_input):
        """Test that print is called once with the correct message for valid key 'B'."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            access_resource('B')
            self.assertEqual(fake_out.getvalue().strip(), 'Access granted to: Resource B')

    @patch('builtins.input', side_effect=['C'])
    def test_print_called_correctly_for_C(self, mock_input):
        """Test that print is called once with the correct message for valid key 'C'."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            access_resource('C')
            self.assertEqual(fake_out.getvalue().strip(), 'Access granted to: Resource C')

    @patch('builtins.input', side_effect=['D'])
    def test_print_called_correctly_for_invalid_key(self, mock_input):
        """Test that print is called once with the correct message for invalid key 'D'."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            access_resource('D')
            self.assertEqual(fake_out.getvalue().strip(), 'Access denied. Invalid key.')

    @patch('builtins.input', side_effect=[''])
    def test_print_called_correctly_for_empty_key(self, mock_input):
        """Test that print is called once with the correct message for empty key."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            access_resource('')
            self.assertEqual(fake_out.getvalue().strip(), 'Access denied. Invalid key.')

# Run the tests
if __name__ == '__main__':
    unittest.main()