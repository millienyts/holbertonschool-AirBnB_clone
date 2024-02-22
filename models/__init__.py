#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel instances"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(expected, str(model))

    def test_save(self):
        """Test the save method updates `updated_at`"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method returns a dictionary with correct keys and formats"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertTrue("created_at" in model_dict and "updated_at" in model_dict)
        self.assertTrue(isinstance(model_dict["created_at"], str) and isinstance(model_dict["updated_at"], str))

if __name__ == "__main__":
    unittest.main()
