#!/usr/bin/python3
"""
File: Test_Amenity.py
Path: app/tests/test_models/Test_Amenity.py
Module: TestAmenity
Description: Test file for Amenity

--- States ---
    test_init()
    test_name_attribute()
    test_to_dict()
    test_str()
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertTrue(hasattr(amenity, 'id'))

    def test_name_attribute(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('name', amenity_dict)

    def test_str(self):
        amenity = Amenity()
        self.assertIsInstance(str(amenity), str)


if __name__ == '__main__':
    unittest.main()
