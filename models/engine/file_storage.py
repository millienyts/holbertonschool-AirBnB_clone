import json
from models.base_model import BaseModel
from models.user import User  # Import additional classes here

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w') as f:
            json_dict = {}
            for key, obj in self.__objects.items():
                json_dict[key] = obj.to_dict()  # Convert object to a dictionary
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists."""
        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, obj_dict in json_dict.items():
                cls_name = obj_dict['__class__']
                cls = eval(cls_name)  # Convert string to class
                self.__objects[key] = cls(**obj_dict)  # Create an instance
        except FileNotFoundError:
            pass
