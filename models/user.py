#!/usr/bin/python3
"""
Module: user
User class that inherits from BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for User"""
        super().__init__(*args, **kwargs)
