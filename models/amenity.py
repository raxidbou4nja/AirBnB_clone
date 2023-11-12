#!/usr/bin/python3
"""
File: Amenity.py
Path: app/models/Amenity.py
Module: Amenity
Description: Amenity class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        amenity_dc = super().to_dict()
        amenity_dc['name'] = self.name
        return amenity_dc
