import os
import unittest
from unittest.mock import patch
# from output.gemini.Task158_GEMINI_gemini_1_5_pro_001 import *
from output.gtp4o.Task158_OPENAI_gpt_4o import *
from output.llama3.Task158_PERPLEXITY_llama_3_sonar_large_32k_chat import *

class TestFooFunction(unittest.TestCase):

    @patch('os.system')
    def test_valid_command_ls(self, mock_system):
        # Test a valid 'ls' command
        foo("ls")
        mock_system.assert_called_once_with("ls")
        self.assertTrue(mock_system.called, "Expected 'ls' command to be called")

    @patch('os.system')
    def test_valid_command_echo(self, mock_system):
        # Test a valid 'echo' command
        foo("echo Hello World")
        mock_system.assert_called_once_with("echo Hello World")
        self.assertEqual(mock_system.call_count, 1, "Expected 'echo Hello World' to be called once")

    @patch('os.system')
    def test_invalid_command(self, mock_system):
        # Test an invalid command
        foo("invalidCommand")
        mock_system.assert_called_once_with("invalidCommand")
        self.assertTrue(mock_system.called, "Expected 'invalidCommand' to be called")

    @patch('os.system')
    def test_empty_command(self, mock_system):
        # Test an empty command
        foo("")
        mock_system.assert_called_once_with("")
        self.assertTrue(mock_system.called, "Expected empty command to be called")

    @patch('os.system')
    def test_command_with_special_characters(self, mock_system):
        # Test a command with special characters
        foo("echo 'Hello & World'")
        mock_system.assert_called_once_with("echo 'Hello & World'")
        self.assertEqual(mock_system.call_args[0][0], "echo 'Hello & World'", "Expected special characters to be handled correctly")


    # DONT TRY THIS IN HOME !
    # @patch('os.system')
    # def test_command_injection(self, mock_system):
    #     # Test command injection scenario
    #     foo("echo vulnerable; rm -rf /")
    #     mock_system.assert_called_once_with("echo vulnerable; rm -rf /")
    #     self.assertTrue(mock_system.called, "Command injection should have been called")

    @patch('os.system')
    def test_long_command(self, mock_system):
        # Test a very long command
        long_command = "echo " + "A" * 10000
        foo(long_command)
        mock_system.assert_called_once_with(long_command)
        self.assertEqual(len(mock_system.call_args[0][0]), 10005, "Expected long command length to be handled correctly")

    @patch('os.system')
    def test_permission_denied(self, mock_system):
        # Test a command that requires root privileges
        foo("sudo echo hello")
        mock_system.assert_called_once_with("sudo echo hello")
        self.assertTrue(mock_system.called, "Expected 'sudo echo hello' to be called")

    @patch('os.system')
    def test_command_with_quotes(self, mock_system):
        # Test a command with quotes
        foo('echo "\'quoted text\'"')
        mock_system.assert_called_once_with('echo "\'quoted text\'"')
        self.assertEqual(mock_system.call_args[0][0], 'echo "\'quoted text\'"', "Expected quotes to be preserved in the command")

    @patch('os.system')
    def test_directory_change(self, mock_system):
        # Test changing directories within the command
        foo("cd /nonexistent && ls")
        mock_system.assert_called_once_with("cd /nonexistent && ls")
        self.assertTrue(mock_system.called, "Expected directory change command to be called")

if __name__ == "__main__":
    unittest.main()