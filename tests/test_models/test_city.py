#!/usr/bin/python3
"""
File: Test_City.py
Path: app/Test_City.py
Module: TestCity
Description: Test file for City

--- States ---
    test_init()
    test_state_id_attribute()
    test_name_attribute()
    test_to_dict()
    test_str()
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def test_init(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertTrue(hasattr(city, 'id'))

    def test_state_id_attribute(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_name_attribute(self):
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        city = City()
        city_dc = city.to_dict()

        self.assertIsInstance(city_dc, dict)
        self.assertIn('__class__', city_dc)
        self.assertIn('created_at', city_dc)
        self.assertIn('updated_at', city_dc)
        self.assertIn('state_id', city_dc)
        self.assertIn('name', city_dc)

    def test_str(self):
        city = City()
        self.assertIsInstance(str(city), str)


if __name__ == '__main__':
    unittest.main()
