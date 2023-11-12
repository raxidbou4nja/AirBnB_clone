#!/usr/bin/python3
"""
File: Test_State.py
Path: app/tests/test_models/Test_State.py
Module: TestState
Description: Test file for State

--- States ---
    test_init()
    test_name_attribute()
    test_to_dict()
    test_str()
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_init(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertTrue(hasattr(state, 'id'))

    def test_name_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        state = State()
        state_dc = state.to_dict()

        self.assertIsInstance(state_dc, dict)
        self.assertIn('__class__', state_dc)
        self.assertIn('created_at', state_dc)
        self.assertIn('updated_at', state_dc)
        self.assertIn('name', state_dc)

    def test_str(self):
        state = State()
        self.assertIsInstance(str(state), str)


if __name__ == '__main__':
    unittest.main()
