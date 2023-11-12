#!/usr/bin/python3
"""
File: State.py
Path: app/models/state.py
Module: state
Description: State class that inherits from BaseModel

--- States ---
    __init__
    to_dict
"""

from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        state_dc = super().to_dict()
        state_dc['name'] = self.name
        return state_dc
