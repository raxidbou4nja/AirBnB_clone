#!/usr/bin/python3
"""
File: Test_Console.py
Path: app/tests/Test_Console.py
Module: TestHBNBCommand
Description: Test file for Console

--- States ---
    setUp()
    tearDown()
    test_quit_command()
    test_EOF_command()
    test_destroy_command()
    test_emptyline_method()
    test_create_command()
    test_show_command()
    test_all_command()
    test_count_command()
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
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

    def test_destroy_command(self):
        with patch('sys.stdout', self.mock_stdout):
            # Create a new BaseModel instance
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()

            instance_id = output.split()[0]

            self.console.onecmd("destroy BaseModel {}".format(instance_id))

    def test_emptyline_method(self):
        with patch('sys.stdout', self.mock_stdout):
            self.console.emptyline()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.console.onecmd("create BaseModel")
        output = self.mock_stdout.getvalue().strip()

        self.assertTrue(output.startswith(""))
