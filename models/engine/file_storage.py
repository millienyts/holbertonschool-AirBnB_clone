#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f'{obj.__class__.__name__}.{obj.id}'
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(type(self).__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in type(self).__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the JSON file (__file_path) exists."""
        try:
            with open(type(self).__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_attrs in obj_dict.items():
                    cls_name = obj_attrs['__class__']
                    cls = eval(cls_name)  # Be cautious with eval(), ensure safe context
                    type(self).__objects[obj_id] = cls(**obj_attrs)
        except FileNotFoundError:
            pass
