#!/usr/bin/python3
"""
Module: __init__.py
"""


# models/__init__.py
try:
    from models.engine import file_storage
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review

    storage = file_storage.FileStorage()
    storage.reload()
except Exception as e:
    pass
