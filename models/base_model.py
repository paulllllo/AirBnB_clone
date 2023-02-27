#!/usr/bin/python3
"""Defines a base class BaseModel for other classes in the web site"""

import uuid
from datetime import datetime


class BaseModel:
    """Public class attributes"""

    """A class that defines a base class for inheritance\
    by other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key !=  "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else :
                        setattr(self, key, value)
        else :
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def save(self):
        """updates the public instance attribute updated_at with\
        the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of\
        __dict__ of the instance"""
        newdict = dict(self.__dict__)
        newdict["__class__"] = self.__class__.__name__
        created_at = self.created_at.isoformat("T", "microseconds")
        updated_at = self.updated_at.isoformat("T", "microseconds")
        newdict["created_at"] = created_at
        newdict["updated_at"] = updated_at

        return newdict

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
