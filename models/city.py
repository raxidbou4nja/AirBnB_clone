#!/usr/bin/python3
"""
Module: city
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for City"""
        super().__init__(*args, **kwargs)