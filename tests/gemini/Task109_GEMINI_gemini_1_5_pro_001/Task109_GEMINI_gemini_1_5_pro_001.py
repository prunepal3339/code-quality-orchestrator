import io
import unittest
from unittest.mock import patch

from output.gemini.Task109_GEMINI_gemini_1_5_pro_001 import validate_email


class TestValidateEmail(unittest.TestCase):

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_valid_email(self, mock_stdout):
    validate_email("test@example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Valid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_valid_email_with_subdomain(self, mock_stdout):
    validate_email("user.name@subdomain.example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Valid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_missing_at(self, mock_stdout):
    validate_email("user.example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_missing_domain(self, mock_stdout):
    validate_email("user@.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_with_spaces(self, mock_stdout):
    validate_email("user @example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_with_special_characters(self, mock_stdout):
    validate_email("user@exa!mple.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_too_short(self, mock_stdout):
    validate_email("a@b.c")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_valid_email_with_long_domain(self, mock_stdout):
    validate_email("user@subdomain.example.long")
    self.assertEqual(mock_stdout.getvalue().strip(), "Valid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_invalid_email_with_multiple_at_symbols(self, mock_stdout):
    validate_email("user@@example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address")

  @patch('sys.stdout', new_callable=io.StringIO)
  def test_valid_email_with_dots_in_local_part(self, mock_stdout):
    validate_email("user.name@example.com")
    self.assertEqual(mock_stdout.getvalue().strip(), "Valid email address")

if __name__ == '__main__':
  unittest.main()