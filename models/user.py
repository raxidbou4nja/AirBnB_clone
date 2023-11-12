#!/usr/bin/python3
"""
File: User.py
Path: app/models/User.py
Module: User
Description: User class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        user_dc = super().to_dict()
        user_dc['email'] = self.email
        user_dc['password'] = self.password
        user_dc['first_name'] = self.first_name
        user_dc['last_name'] = self.last_name
        return user_dc
