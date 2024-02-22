#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the base model class"""
    
    def test_id_creation(self):
        """Test id is created and is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
    
    def test_datetime_creation(self):
        """Test created_at and updated_at are datetime objects"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
