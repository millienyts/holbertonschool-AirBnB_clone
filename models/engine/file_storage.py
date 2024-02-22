import json
from models.base_model import BaseModel
from models.user import User  # Import additional classes as needed

class FileStorage:
    __file_path = "file.json"  # Path to the JSON file for storing objects
    __objects = {}  # Dictionary to store all objects by <class name>.id

    # A dictionary mapping class names to classes, used for deserialization
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        # Add other classes to this dictionary as you create them
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds an object to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file (__file_path) to __objects if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                cls_name = obj_data['__class__']
                if cls_name in self.class_dict:
                    cls = self.class_dict[cls_name]
                    self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass
