#!/usr/bin/python3
"""
File: Review.py
Path: app/models/Review.py
Module: Review
Description: Review class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        review_dc = super().to_dict()
        review_dc['place_id'] = self.place_id
        review_dc['user_id'] = self.user_id
        review_dc['text'] = self.text
        return review_dc
