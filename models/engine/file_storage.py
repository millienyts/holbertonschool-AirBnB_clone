#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
