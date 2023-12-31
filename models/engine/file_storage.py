#!/usr/bin/python3
"""
File: File_Storage.py
Path: app/models/engine/File_Storage.py
Module: FileStorage
Description: file to storage data in file.json

--- States ---
    all()
    new()
    save()
    reload()
"""

import os
from os.path import exists
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        self.save()

    def save(self):
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        if exists(FileStorage.__file_path):
            with open(
                FileStorage.__file_path, mode='r', encoding='utf-8'
            ) as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_instance


FileStorage.classes['BaseModel'] = BaseModel
FileStorage.classes['User'] = User
FileStorage.classes['State'] = State
FileStorage.classes['City'] = City
FileStorage.classes['Amenity'] = Amenity
FileStorage.classes['Place'] = Place
FileStorage.classes['Review'] = Review
