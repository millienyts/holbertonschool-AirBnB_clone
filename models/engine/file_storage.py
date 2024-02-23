#!/usr/bin/python3
"""
    class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
"""

import json
import os
from models.base_model import BaseModel


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

if __name__ == "__main__":
    import unittest

    class TestFileStorage(unittest.TestCase):
        def setUp(self):
            self.storage = FileStorage()
            self.model = BaseModel()

        def test_file_path(self):
            self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

        def test_objects(self):
            self.assertIsInstance(FileStorage._FileStorage__objects, dict)

        def test_all(self):
            all_objects = self.storage.all()
            self.assertIsInstance(all_objects, dict)

        def test_new(self):
            initial_count = len(self.storage.all())
            new_model = BaseModel()
            self.storage.new(new_model)
            new_count = len(self.storage.all())
            self.assertEqual(new_count, initial_count + 1)

        def test_save(self):
            self.model.name = "Test Model"
            self.model.save()
            self.assertTrue(os.path.exists("file.json"))
            with open("file.json", "r") as f:
                data = json.load(f)
                key = f"BaseModel.{self.model.id}"
                self.assertIn(key, data)
                self.assertEqual(data[key]["name"], "Test Model")

        def test_reload(self):
            self.assertTrue(len(self.storage.all()) > 0)
            self.model.save()
            with open("file.json", "r") as f:
                data = json.load(f)
            key = f"BaseModel.{self.model.id}"
            data[key]['custom_attribute'] = "Test Reload"
            with open("file.json", "w") as f:
                json.dump(data, f)
            self.storage.reload()
            all_objects = self.storage.all()
            self.assertIn(key, all_objects)
            loaded_model = all_objects[key]
            self.assertTrue('custom_attribute' in loaded_model.to_dict())
            self.assertEqual(loaded_model.to_dict()['custom_attribute'], "Test Reload")

    unittest.main()
