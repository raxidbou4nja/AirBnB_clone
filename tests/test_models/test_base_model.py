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
        objM = BaseModel()
        str_representation = str(objM)
        expected_representation = "[BaseModel] ({}) {}"
        .format(objM.id, objM.__dict__)
        self.assertEqual(str_representation, expected_representation)


if __name__ == '__main__':
    unittest.main()
