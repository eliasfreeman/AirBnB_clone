#!/usr/bin/python3

"""
    File storage module
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
        This module handles file storage
        It serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            Returns the "__objects" dictionary
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in "__objects" the "obj" with key "<obj class_name>.id"
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            Serialize "__objects" and save to json file (path: __file_path)
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
            Deserialize the json file to "__objects" only if
            "__file_path" exists. Otherwise, do nothing
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)
            for key, value in dict_obj.items():
                self.__objects[key] = eval(key.split(".")[0])(**value)
        except FileNotFoundError:
            pass
