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

    def test_all_method(self):
        """Test the all method returns all objects."""
        self.assertEqual(len(self.storage.all()), 0)
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new_method(self):
        """Test the new method adds objects correctly."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_objects_type(self):
        """Test that __objects is a dictionary."""
        self.assertTrue(isinstance(self.storage.all(), dict))

    def test_save_creates_file(self):
        """Test that save method creates a file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_method(self):
        """Test reloading objects from a file."""
        obj = BaseModel()
        obj.name = "Holberton"
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, objects)
        reloaded_obj = objects[key]
        self.assertEqual(reloaded_obj.name, obj.name)

if __name__ == "__main__":
    unittest.main()
