#!/usr/bin/python3

"""
Implements the FileStorage engine for data persistence using JSON files.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the objects to the JSON file.
        """
        with open(self.__file_path, "w") as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """
        Deserialize the JSON file to objects, if the file exists.
        """
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass
