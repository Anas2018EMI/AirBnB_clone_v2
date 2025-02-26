#!/usr/bin/python3
"""
This module defines a class to manage file storage for the hbnb clone.
"""
import json


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If a class is provided, filters objects of that class.
        """
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Saves storage dictionary to a JSON file.
        """
        with open(self.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """
        Loads storage dictionary from a JSON file.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                self.__objects = {k: classes[v['__class__']](
                    **v) for k, v in temp.items()}
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it exists.
        Does nothing if obj is None.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)

    def close(self):
        """
        Call reload() method for deserializing the JSON file to objects.
        """
        self.reload()
