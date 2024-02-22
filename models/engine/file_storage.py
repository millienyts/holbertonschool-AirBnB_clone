#!/usr/bin/python3
import json

class FileStorage:
    """Handles long-term storage of all class instances."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary `__objects`."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Adds new object to the storage dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
    
    def save(self):
        """Serializes `__objects` to the JSON file."""
        with open(self.__
