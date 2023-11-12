#!/usr/bin/python3
"""
File: Test_Review.py
Path: app/tests/test_models/Test_Review.py
Module: TestReview
Description: Test file for Review

--- States ---
    test_init()
    test_place_id_attribute()
    test_user_id_attribute()
    test_text_attribute()
    test_to_dict()
    test_str()
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_init(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertTrue(hasattr(review, 'id'))

    def test_place_id_attribute(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")

    def test_user_id_attribute(self):
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")

    def test_text_attribute(self):
        review = Review()
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        review = Review()
        review_dc = review.to_dict()

        self.assertIsInstance(review_dc, dict)
        self.assertIn('__class__', review_dc)
        self.assertIn('created_at', review_dc)
        self.assertIn('updated_at', review_dc)
        self.assertIn('place_id', review_dc)
        self.assertIn('user_id', review_dc)
        self.assertIn('text', review_dc)

    def test_str(self):
        review = Review()
        self.assertIsInstance(str(review), str)


if __name__ == '__main__':
    unittest.main()
