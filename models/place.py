#!/usr/bin/python3
"""
File: Place.py
Path: app/models/Place.py
Module: Place
Description: Place class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        place_dc = super().to_dict()
        place_dc['city_id'] = self.city_id
        place_dc['user_id'] = self.user_id
        place_dc['name'] = self.name
        place_dc['description'] = self.description
        place_dc['number_rooms'] = self.number_rooms
        place_dc['number_bathrooms'] = self.number_bathrooms
        place_dc['max_guest'] = self.max_guest
        place_dc['price_by_night'] = self.price_by_night
        place_dc['latitude'] = self.latitude
        place_dc['longitude'] = self.longitude
        place_dc['amenity_ids'] = self.amenity_ids
        return place_dc
