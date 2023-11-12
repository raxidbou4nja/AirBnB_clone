#!/usr/bin/python3
"""
File: Test_Place.py
Path: app/tests/test_models/Test_Place.py
Module: TestPlace
Description: Test file for Place

--- States ---
    test_init()
    test_city_id_attribute()
    test_user_id_attribute()
    test_name_attribute()
    test_description_attribute()
    test_number_rooms_attribute()
    test_number_bathrooms_attribute()
    test_max_guest_attribute()
    test_price_by_night_attribute()
    test_latitude_attribute()
    test_longitude_attribute()
    test_amenity_ids_attribute()
    test_to_dict()
    test_str()
"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    def test_init(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertTrue(hasattr(place, 'id'))

    def test_city_id_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")

    def test_user_id_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")

    def test_name_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")

    def test_description_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")

    def test_number_rooms_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        place = Place()
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        place = Place()
        amenity_dc = place.to_dict()

        self.assertIsInstance(amenity_dc, dict)
        self.assertIn('__class__', amenity_dc)
        self.assertIn('created_at', amenity_dc)
        self.assertIn('updated_at', amenity_dc)
        self.assertIn('city_id', amenity_dc)
        self.assertIn('user_id', amenity_dc)
        self.assertIn('name', amenity_dc)
        self.assertIn('description', amenity_dc)
        self.assertIn('number_rooms', amenity_dc)
        self.assertIn('number_bathrooms', amenity_dc)
        self.assertIn('max_guest', amenity_dc)
        self.assertIn('price_by_night', amenity_dc)
        self.assertIn('latitude', amenity_dc)
        self.assertIn('longitude', amenity_dc)
        self.assertIn('amenity_ids', amenity_dc)

    def test_str(self):
        place = Place()
        self.assertIsInstance(str(place), str)


if __name__ == '__main__':
    unittest.main()
