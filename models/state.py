#!/usr/bin/python3
"""
Module: state
State class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for State"""
        super().__init__(*args, **kwargs)
