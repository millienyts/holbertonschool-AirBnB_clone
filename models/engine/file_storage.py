#!/usr/bin/python3
"""
    class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
# Importing all possible classes
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):

        """Adds an object to the __objects dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):

        """Serializes __objects to the JSON file (__file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):

        """Deserializes the JSON file (__file_path) to __objects if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for obj_id, obj_data in objects.items():
                cls_name = obj_data['__class__']
                cls = globals().get(cls_name)
                if cls:
                    FileStorage.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass
