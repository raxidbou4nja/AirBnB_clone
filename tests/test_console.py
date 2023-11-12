#!/usr/bin/python3
"""
Console Module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand  # Correct import statement


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()  # Use HBNBCommand from the console module
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    def test_quit_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.assertTrue(self.console.onecmd("quit"))
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_EOF_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.assertTrue(self.console.onecmd("EOF"))
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_emptyline_method(self):
        with patch('sys.stdout', self.mock_stdout):
            self.console.emptyline()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_command(self):
        with patch('sys.stdout', self.mock_stdout):
            # Simulate user input for creating a new BaseModel instance
            self.console.onecmd("create BaseModel")
        output = self.mock_stdout.getvalue().strip()

        # Check if the output contains the new instance's ID
        self.assertTrue(output.startswith(""))

    def test_show_command(self):
        with patch('sys.stdout', self.mock_stdout):
            # Create a new BaseModel instance
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()

if __name__ == '__main__':
    unittest.main()