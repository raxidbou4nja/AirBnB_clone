#!/usr/bin/python3
"""
Module: test_file_storage
Test cases for the FileStorage class
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.file_storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj3 = State()
        self.obj4 = City()
        self.obj5 = Amenity()
        self.obj6 = Place()
        self.obj7 = Review()
        FileStorage.classes['BaseModel'] = BaseModel
        FileStorage.classes['User'] = User
        FileStorage.classes['State'] = State
        FileStorage.classes['City'] = City
        FileStorage.classes['Amenity'] = Amenity
        FileStorage.classes['Place'] = Place
        FileStorage.classes['Review'] = Review

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        self.file_storage.new(self.obj1)
        all_objects = self.file_storage.all()
        self.assertIn('BaseModel.{}'.format(self.obj1.id), all_objects)

    def test_save_reload(self):
        self.file_storage.new(self.obj2)
        self.file_storage.new(self.obj3)
        self.file_storage.new(self.obj4)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn('User.{}'.format(self.obj2.id), all_objects)
        self.assertIn('State.{}'.format(self.obj3.id), all_objects)
        self.assertIn('City.{}'.format(self.obj4.id), all_objects)

    def test_classes_attribute(self):
        classes = FileStorage.classes
        self.assertIsInstance(classes, dict)
        self.assertIn('BaseModel', classes)
        self.assertIn('User', classes)
        self.assertIn('State', classes)
        self.assertIn('City', classes)
        self.assertIn('Amenity', classes)
        self.assertIn('Place', classes)
        self.assertIn('Review', classes)

    def test_save_reload_empty(self):
        # Test saving and reloading when no objects are present
        self.file_storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_amenity_save_reload(self):
        amenity = Amenity()
        self.file_storage.new(amenity)
        self.file_storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn('Amenity.{}'.format(amenity.id), all_objects)

    def test_place_save_reload(self):
        place = Place()
        self.file_storage.new(place)
        self.file_storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn('Place.{}'.format(place.id), all_objects)

    def test_review_save_reload(self):
        review = Review()
        self.file_storage.new(review)
        self.file_storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn('Review.{}'.format(review.id), all_objects)

    def test_file_path(self):
        file_path = self.file_storage._FileStorage__file_path
        self.assertEqual(file_path, "file.json")

    def test_objects_attribute(self):
        objects = self.file_storage._FileStorage__objects
        self.assertGreater(len(objects), 1)

    def test_reload_method(self):
        self.file_storage.new(BaseModel())
        self.file_storage.save()
        self.file_storage.reload()
        result = "OK" if self.file_storage._FileStorage__objects else ""
        self.assertEqual(result, "OK")

if __name__ == '__main__':
    unittest.main()
