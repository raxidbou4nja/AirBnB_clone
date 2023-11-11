#!/usr/bin/python3
"""
Module: review
Review class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for Review"""
        super().__init__(*args, **kwargs)