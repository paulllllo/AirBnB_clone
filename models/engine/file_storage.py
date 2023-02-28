#!/usr/bin/python3
"""Converts instance to JSON file and vice-versa"""

import json
import os.path


class FileStorage:
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    """A class that converts a class instance to a JSON file\
    and vice-versa"""

    """Public instance methods"""
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = f'{obj["__class__"]}.{obj["id"]}'
        self.__objects[obj_name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_file = open(self.__file_path, "w")
        json.dump(self.__objects, json_file)
        json_file.close()

    def reload(self):
        """deserializes the JSON file to __objects\
        (only if the JSON file (__file_path) exists"""
        if os.path.isfile(self.__file_path):
            json_file = open(self.__file_path)
            self.__objects = json.load(json_file)
