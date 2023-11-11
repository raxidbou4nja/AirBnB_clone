#!/usr/bin/python3
"""
Module: amenity
Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for Amenity"""
        super().__init__(*args, **kwargs)