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

