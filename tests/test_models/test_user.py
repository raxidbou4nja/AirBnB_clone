#!/usr/bin/python3
"""
File: Test_User.py
Path: app/tests/test_models/Test_User.py
Module: TestUser
Description: Test file for User

--- States ---
    test_init()
    test_email_attribute()
    test_password_attribute()
    test_first_name_attribute()
    test_last_name_attribute()
    test_to_dict()
    test_str()
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def test_init(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertTrue(hasattr(user, 'id'))

    def test_email_attribute(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")

    def test_password_attribute(self):
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")

    def test_first_name_attribute(self):
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        user = User()
        user_dc = user.to_dict()

        self.assertIsInstance(user_dc, dict)
        self.assertIn('__class__', user_dc)
        self.assertIn('created_at', user_dc)
        self.assertIn('updated_at', user_dc)
        self.assertIn('email', user_dc)
        self.assertIn('password', user_dc)
        self.assertIn('first_name', user_dc)
        self.assertIn('last_name', user_dc)

    def test_str(self):
        user = User()
        self.assertIsInstance(str(user), str)


if __name__ == '__main__':
    unittest.main()
