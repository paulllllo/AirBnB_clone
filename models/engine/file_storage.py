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
        #print("**[Inside file_storage.py] [Inside new method]**")
        obj_name = f'{obj["__class__"]}.{obj["id"]}'
        self.__objects[obj_name] = obj

    def update(self, classname, id, attr_name, attr_value):
        if attr_name in self.__objects[f'{classname}.{id}']:
            attr_type = type(self.__objects[f'{classname}.{id}'][attr_name])
            self.__objects[f'{classname}.{id}'][attr_name] = attr_type(attr_value)
        self.__objects[f'{classname}.{id}'][attr_name] = attr_value

    def view(self, classname, id):
        #print(f'**__objects = {self.__objects} classname = {classname}, id = {id}')
        if f'{classname}.{id}' in self.__objects:
            return self.__objects[f'{classname}.{id}']

    def delete(self, classname, id):
        """Deletes an entry from __objects based on classname.id as key"""
        if f'{classname}.{id}' in self.__objects:
            del self.__objects[f'{classname}.{id}']
            self.save()
            return True

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_file = open(self.__file_path, "w")
        json.dump(self.__objects, json_file)
        json_file.close()

    def exists(self, classname, id):
        return f'{classname}.{id}' in self.__objects

    def reload(self):
        """deserializes the JSON file to __objects\
        (only if the JSON file (__file_path) exists"""
        if os.path.isfile(self.__file_path):
            json_file = open(self.__file_path)
            self.__objects = json.load(json_file)
