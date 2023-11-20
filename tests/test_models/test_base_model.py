#!/usr/bin/python3
"""
File: Test_Base_Model.py
Path: app/tests/test_models/Test_Base_Model.py
Module: TestBaseModel
Description: Test file for BaseModel

--- States ---
    test_init()
    test_str()
    test_save()
    test_to_dict()
"""
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        objM = BaseModel()
        self.assertIsNotNone(objM.id)
        self.assertIsInstance(objM.created_at, datetime)
        self.assertIsInstance(objM.updated_at, datetime)
        self.assertTrue(hasattr(objM, '__class__'))

    def test_str(self):
        objM = BaseModel()
        self.assertIsInstance(str(objM), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        objM = BaseModel()
        objM.save()
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        objM = BaseModel()
        objM_dc = objM.to_dict()
        self.assertIsInstance(objM_dc, dict)
        self.assertIn('__class__', objM_dc)
        self.assertIn('created_at', objM_dc)
        self.assertIn('updated_at', objM_dc)

    def test_str(self):
        # Create a BaseModel with known values
        created_at = datetime(2023, 11, 14, 0, 0, 0)
        updated_at = datetime(2023, 11, 14, 0, 1, 0)
        objM = BaseModel(created_at=created_at, updated_at=updated_at)

        # Get the string representation
        str_representation = str(objM)

        # Manually format the expected representation with the correct datetime format
        expected_representation = "[BaseModel] ({}) {{'updated_at': '{}', 'created_at': '{}', 'id': '{}'}}".format(
            objM.id,
            updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            created_at.strftime('%Y-%m-%d %H:%M:%S'),
            objM.id
        )

        # Assert that the actual and expected representations match
        self.assertEqual(str_representation, expected_representation)

if __name__ == '__main__':
    unittest.main()
