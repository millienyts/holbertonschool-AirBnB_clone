#!/usr/bin/python3
import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage class."""

    def setUp(self):
        """Runs before each test to ensure a fresh environment."""
        self.storage = FileStorage()
        # Ensure the file.json is deleted before each test to start fresh
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save_and_reload(self):
        """Test saving objects to file and reloading them."""
        # Create a new BaseModel object and save it
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        self.storage.new(obj)
        self.storage.save()

        # Create a new FileStorage instance and reload data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the new storage has the previously saved object
        objects = new_storage.all()
        self.assertTrue(isinstance(objects, dict))
        self.assertTrue(f"BaseModel.{obj.id}" in objects)

        # Verify that the reloaded object matches the original object
        reloaded_obj = objects[f"BaseModel.{obj.id}"]
        self.assertEqual(reloaded_obj.name, "Holberton")
        self.assertEqual(reloaded_obj.my_number, 89)

    def tearDown(self):
        """Runs after each test to clean up."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

if __name__ == "__main__":
    unittest.main()
