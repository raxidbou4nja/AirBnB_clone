#!/usr/bin/python3
"""
File: City.py
Path: app/models/City.py
Module: City
Description: City class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        city_dc = super().to_dict()
        city_dc['state_id'] = self.state_id
        city_dc['name'] = self.name
        return city_dc
