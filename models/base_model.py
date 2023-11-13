#!/usr/bin/python3
"""
File: BaseModel.py
Path: app/models/BaseModel.py
Module: BaseModel
Description: BaseModel class

--- States ---
    __init__
    __str__
    save
    to_dict
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        if isinstance(value, datetime):
                            setattr(self, key, value)
                        else:
                            setattr(
                                self,
                                key,
                                datetime.strptime(
                                    str(value), format
                                )
                            )
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        cleaned_dc = {
            str(key).strip("{}':"): str(value).strip("{}'")
            for key, value in self.__dict__.items()
        }
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, cleaned_dc
        )

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        baseM_dc = self.__dict__.copy()
        baseM_dc['__class__'] = self.__class__.__name__
        baseM_dc['created_at'] = self.created_at.isoformat()
        baseM_dc['updated_at'] = self.updated_at.isoformat()
        return baseM_dc
