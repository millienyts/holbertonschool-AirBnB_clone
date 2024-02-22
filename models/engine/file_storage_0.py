#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """A class that serializes instances to a JSON file & deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key '<obj class name>.id'"""
        if obj:
            obj_id = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[obj_id] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')"""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for obj_id, obj_data in objects.items():
                class_name = obj_data['__class__']
                if class_name == 'BaseModel':
                    obj = BaseModel(**obj_data)
                    FileStorage.__objects[obj_id] = obj
        except FileNotFoundError:
            pass
